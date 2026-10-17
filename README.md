# AWS Auto-Scaling Web Application with Load Balancer

A Python Flask web application designed to demonstrate cloud deployment,
application health checks, load balancing, and automatic scaling using AWS.

## Project Overview

This project aims to deploy a web application on Amazon EC2 and prepare it
for scalable operation using an Application Load Balancer and an EC2 Auto
Scaling Group.

The application includes a cloud status dashboard and a health-check endpoint.

## Technologies Used

- Python
- Flask
- Gunicorn
- HTML5 and CSS3
- Amazon EC2
- Application Load Balancer
- EC2 Auto Scaling
- Amazon CloudWatch
- Git and GitHub

## Current Features

- Responsive cloud status dashboard.
- Server hostname display.
- Application health-check endpoint.
- JSON health-check response.
- Timestamp showing when the dashboard was generated.

## Application Endpoints

### Dashboard

`GET /`

Displays the cloud status dashboard.

### Health Check

`GET /health`

Returns the application health status and server hostname.

Example response:

```json
{
  "status": "healthy",
  "server": "example-server"
}
