# BizzNexx Backend

This folder contains the first Django backend shape for the BizzNexx prototype.

It is intentionally model-first. The goal is to stabilize the ontology before adding a full API.

## Intended Stack

- Django
- Django REST Framework
- PostgreSQL
- OpenAI API for message generation

## Domain Apps

- `businesses`: business profile, catalogue, trust proof, inquiries, leads, payments, and messages

## Next Backend Steps

1. Create Django project with `django-admin startproject bizznexx_backend .`
2. Install Django REST Framework.
3. Add the models from `businesses/models.py`.
4. Add serializers and viewsets for the frontend.
5. Add seed data matching the React sample business.
