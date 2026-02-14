# Django_project

# Debt Management System

A Django-based web application for managing debtors and tracking outstanding debts, designed for debt collection agencies.

## 🚀 Project Status

**Current Version:** v1.0 - Full CRUD Implementation

This is a learning project built to understand Django fundamentals through a real-world use case.

## ✨ Features

### Currently Implemented
- ✅ **Complete CRUD operations** for debtors
  - Create new debtors
  - View debtor list
  - View individual debtor details
  - Edit debtor information
  - Delete debtors (with confirmation)
- ✅ **Django Admin panel** integration
- ✅ **Form validation** (basic Django validation)
- ✅ **Database models** with proper field types and constraints

### Coming Soon
1. 🔄 **Custom Validations**
   - Debt amount must be greater than 0
   - Argentine DNI format validation
   - Enhanced email uniqueness validation
   - Phone number format validation

2. 🔄 **User Feedback Messages**
   - Success messages ("Debtor created successfully")
   - Error messages ("DNI already exists")
   - Delete confirmations
   - Update notifications

3. 🔄 **Payment Tracking Model**
   - Related Payment model (ForeignKey relationship)
   - Track partial payments
   - Payment history per debtor
   - Automatic debt balance calculation

### Future Enhancements (Planned)
- Search functionality (by DNI, name)
- Filters (by status, debt amount)
- Pagination for large datasets
- UI improvements with Bootstrap/CSS
- Export functionality (CSV, PDF)

## 🛠️ Tech Stack

- **Framework:** Django 6.0.1
- **Language:** Python 3.14
- **Database:** SQLite3
- **Template Engine:** Django Templates

## 🚦 Getting Started

### Prerequisites
- Python 3.14+
- pip
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/FeHa1/Djando_proyect.git
cd Djando_proyect
```

2. **Create and activate virtual environment**
```bash
python3 -m venv Django_venv
source Django_venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies**
```bash
pip install django
```

4. **Run migrations**
```bash
python3 manage.py migrate
```

5. **Create a superuser** (for admin access)
```bash
python3 manage.py createsuperuser
```

6. **Run the development server**
```bash
python3 manage.py runserver
```

7. **Access the application**
- Main app: http://127.0.0.1:8000/deudores/
- Admin panel: http://127.0.0.1:8000/admin/

## 📝 Usage

### Managing Debtors

1. **Add a new debtor**: Click "Agregar Nuevo Deudor" from the list view
2. **View debtor details**: Click "Ver detalle" on any debtor in the list
3. **Edit debtor**: Click "Editar" from the detail view or list view
4. **Delete debtor**: Click "Eliminar" from the detail view (requires confirmation)

### Admin Panel

Access the admin panel at `/admin/` to:
- Manage debtors with advanced filtering
- View all database records
- Bulk operations

## 🎯 Learning Goals

This project was built to practice and understand:
- Django MVT (Model-View-Template) architecture
- ORM and database operations
- Form handling and validation
- URL routing and view functions
- Template rendering and template tags
- Admin customization
- CRUD operations

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome!

## 📜 License

This project is for educational purposes.

## 👨‍💻 Author

**Fede** - Learning Django through practical application development
