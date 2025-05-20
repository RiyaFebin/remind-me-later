#  Remind-Me-Later

Remind-Me-Later is a simple Django-based REST API that allows users to create reminders by submitting a message, date, time, and preferred reminder method (SMS or Email). This project focuses only on storing reminder requests in the database — actual message delivery is not implemented.

---

##  Features

- Submit a message with date and time.
- Choose a reminder method (`email` or `sms`).
- Store reminders in a database.
- Designed for future expansion (e.g., push notifications, WhatsApp reminders).

---

##  Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite3 (default, can be switched to MySQL or PostgreSQL)

---

##  API Endpoint

### `POST /api/reminders/create/`

**Request JSON:**

```json
{
  
  "date": "2025-05-22",
  "time": "15:30:00",
  "message": "Doctor appointment",
  "remind_by": "email"
}
