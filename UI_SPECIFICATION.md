# User Management Screen - UI Specification Document

## 1. Project Overview
This document defines the UI requirements for the User Management interface. The screen allows administrators to manage users and their roles efficiently.

## 2. UI Components & Layout
The interface is divided into a **User List Table** on the left and a **User Entry Form** on the right.

### 2.1 User List (Left Section)
* **Table Columns:** ID, User Name, Email, Enabled.
* **Action Bar:** Contains a `+ New User` button and a `Hide Disabled User` checkbox.
* **Interactions:** Each column header features sorting (up/down arrows) and filtering (funnel icon) capabilities.

### 2.2 New User Form (Right Section)
* **Header:** Titled "New User".
* **Input Fields:**
    - **Username:** Text field.
    - **Display Name:** Text field.
    - **Phone:** Text field.
    - **Email:** Text field with validation.
* **Role Selection:** A dropdown menu containing "Guest", "Admin", and "SuperAdmin".
* **Status:** An "Enabled" checkbox to set user activity.
* **Save Action:** A "Save User" button located at the top-right corner.

## 3. Behavioral Requirements
* **Initial State:** On load, the table fetches all users. The "Hide Disabled User" filter is active by default.
* **Form Logic:** The "Save User" button remains inactive until mandatory fields (Username, Email, Roles) are filled.
