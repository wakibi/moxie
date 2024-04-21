### To run the app
- Make sure you have docker installed
- Clone / download repo from github
- Switch directory to director of the app
- Run `docker compose build`
- Run `docker compose up` (make sure port 8000 is open as that's where the app runs)

The `BASE_URL` for the API is `localhost:8000/api/medspa`. I have deliberately disabled authorisation in the app to enable easy testing of the important aspects. No token / username requited.

To list services, point the URL to (using Postman or your favorite browser) `BASE_URL/services/` using `GET` method
To create a service, point the URL to `BASE_URL/services/` using `POST` method. The body should have the data for the new medspa
To get service details by ID, point the URL to `BASE_URL/services/<id-of-service>/` using `GET` method
To update service by ID, point the URL to `BASE_URL/services/<id-of-service>/` using `PUT` or `PATCH` method
To list services for a particular medspa, point the URL to `BASE_URL/services/medspa/<id-of-spa>/` using `GET` method

For Appointments, follow the following;

To list appointments, point the URL to (using Postman or your favorite browser) `BASE_URL/appointments/` using `GET` method
To create an appointment, point the URL to `BASE_URL/appointments/` using `appointments` method. The body should have the data for the new medspa
To get appointment details by ID, point the URL to `BASE_URL/appointments/<id-of-appt>/` using `GET` method
To update appointment by ID, point the URL to `BASE_URL/services/<id-of-appt>/` using `PUT` or `PATCH` method
To list appointments of a particular status, point the URL to `BASE_URL/appointments/date/<start>/` using `GET` method. Start is a date in the `Y-m-d` formart e.g `2024-03-01` is March, 1st, 2024.



