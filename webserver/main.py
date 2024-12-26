from flask import Flask
import time

web = Flask(__name__)


def bubble_sort():
    temp_list = [i for i in range(2000, -1, -1)]
    n = len(temp_list)

    for i in range(n):
        for j in range(n-i-1):
            if temp_list[j] > temp_list[j+1]:
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                swapped = True

        if (swapped == False):
            break
    
    return temp_list

@web.route('/heavy-task', methods=['GET'])
def heavy_task():
    temp_list = bubble_sort()
    return f"Heavy work has been completed! temp_list = {temp_list[0:3]},...,{temp_list[997:1000]}", 200

@web.route('/', methods=['GET'])
def home():
    return "This is a test server for our DDoS protection application."

if __name__ == '__main__':
    web.run(host='0.0.0.0', port=8000, threaded=True)