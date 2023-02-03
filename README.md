# F1-report-Api

It was also my task from the course and it was based on the previous project (F1-report)
In that project I used Flask for creating app, flask-restful for creating class for api, flasgger for creating swagger and unittest for testing. 


![image](https://user-images.githubusercontent.com/94606127/216643309-d3ef009c-820d-4c3b-a56c-b81ea0574f9c.png)


I used the previous code for creating a report and list of drivers with links. In that project I added Rest Api and swagger. You need to use route '/Apidocs' for openning UI Swagger and get next methods

![photo_2023-02-03_17-16-39](https://user-images.githubusercontent.com/94606127/216641270-a4f1434c-1be8-4acd-9ee6-82698ee5392c.jpg)

You can also choose the type of data that returns XML or JSON

![photo_2023-02-03_17-27-52](https://user-images.githubusercontent.com/94606127/216641889-894a7605-08c1-4f0b-b135-0e4eb4d2318f.jpg)


Another way is using simple routes for getting information

http://127.0.0.1:2000/report - returns all report

http://127.0.0.1:2000/report/{ID}  - returns information about a specific driver (for exemple http://127.0.0.1:2000/report/SVF)

http://127.0.0.1:2000/drivers  - returns the list of drivers and links to each of them on Wiki

http://127.0.0.1:2000/drivers/{ID}  - returns information about a specific driver (for exemple http://127.0.0.1:2000/drivers/SVF)
