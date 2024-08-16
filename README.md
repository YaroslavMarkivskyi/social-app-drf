# Social Media App

This project is a modern social media platform built using Django Rest Framework, designed for scalability and efficiency. The app features comprehensive user interactions like profile management, article posting, bookmarking, rating, and more.

## 🚀 Features

- **User Authentication:** JWT-based authentication with full registration, login, and password management.
- **Profile Management:** View, update profiles, follow and unfollow users.
- **Article Publishing:** Create, update, delete, and interact with articles.
- **Bookmarking:** Save and manage articles for later.
- **Article Ratings:** Rate articles to provide feedback.
- **Elastic Search Integration:** Perform fast and powerful searches through articles.
- **Asynchronous Background Tasks:** Handle background tasks like email notifications with Celery and Redis.
- **API Documentation:** Redoc-powered documentation for a smooth developer experience.

## 🛠️ Tech Stack

- **Backend:** Python, Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Task Queue:** Celery, Redis
- **Email Testing:** MailHog
- **Containerization:** Docker
- **Monitoring and Management:** Flower
- **Search Engine:** Elasticsearch
- **Proxy:** Nginx

## 📂 URL Endpoints
#### Authentication & User Management
- **User Details:** `/api/v1/auth/user/`
- **Authentication:** `/api/v1/auth/`
- **Registration:** `/api/v1/auth/registration/`
- **Password Reset:** `/api/v1/auth/password/reset/confirm/<uidb64>/<token>/`
#### Profiles
- **View All Profiles:** `/api/v1/profiles/all/`
- **My Profile:** `/api/v1/profiles/me/`
- **Update Profile:** `/api/v1/profiles/me/update/`
- **Followers:** `/api/v1/profiles/me/followers/`
- **Follow:** `/api/v1/profiles/<uuid:user_id>/follow/`
- **Unfollow:** `/api/v1/profiles/<uuid:user_id>/unfollow/`
#### Articles
- **List & Create Articles:** `/api/v1/articles/`
- **Retrieve, Update & Delete Article:** `/api/v1/articles/<uuid:id>/`
- **Clap Article:** `/api/v1/articles/<uuid:article_id>/clap/`
#### Bookmarks
- **Bookmark Article:** `/api/v1/bookmarks/bookmark_article/<uuid:article_id>/`
- **Remove Bookmark:** `/api/v1/bookmarks/remove_bookmark/<uuid:article_id>/`
#### Ratings
- **Rate Article:** `/api/v1/ratings/rate_article/<uuid:article_id>/`
#### Responses
- **View & Create Responses:** `/api/v1/responses/article/<uuid:article_id>/`
- **Update & Delete Response:** `/api/v1/responses/<uuid:id>/`
#### Search
- **Search Articles:** `/api/v1/elastic/search/`
#### API Documentation
- **Redoc Documentation:** `/redoc/`

## 📦 Installation 
Clone the repository:
```bash
git clone https://github.com/YaroslavMarkivskyi/social-media-app-drf.git
```
Navigate to the project directory:
```bash
cd social-media-app-drf
```
Set up and run the application using Docker Compose:
```bash
docker-compose -f local.yml up --build
```
Access the application at and read documentation
[http://localhost:8080/redoc](http://localhost:8080/redoc)
