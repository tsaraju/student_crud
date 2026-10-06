Student CRUD API

Create a FastAPI application for managing students.

Required APIs

POST /students

GET /students

GET /students/{student_id}

PUT /students/{student_id}

DELETE /students/{student_id}

Student fields can include id, name, email, age, and course. Use Pydantic validation and return appropriate HTTP status codes.

Sample Output:
PS F:\Euron\GitHub\api\student_crud> uv run uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['F:\\Euron\\GitHub\\api\\student_crud']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [13424] using WatchFiles
INFO:     Started server process [9152]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:55924 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:55924 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:56892 - "POST /students HTTP/1.1" 201 Created
INFO:     127.0.0.1:61260 - "POST /students HTTP/1.1" 201 Created
INFO:     127.0.0.1:58552 - "POST /students HTTP/1.1" 201 Created
INFO:     127.0.0.1:49555 - "GET /students HTTP/1.1" 200 OK
INFO:     127.0.0.1:62728 - "GET /students/2 HTTP/1.1" 200 OK
INFO:     127.0.0.1:62660 - "PUT /students/2 HTTP/1.1" 200 OK
INFO:     127.0.0.1:54359 - "PUT /students/2 HTTP/1.1" 200 OK
INFO:     127.0.0.1:52873 - "GET /students/2 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60723 - "DELETE /students/3 HTTP/1.1" 204 No Content
INFO:     127.0.0.1:53769 - "GET /students HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [9152]
INFO:     Stopping reloader process [13424]