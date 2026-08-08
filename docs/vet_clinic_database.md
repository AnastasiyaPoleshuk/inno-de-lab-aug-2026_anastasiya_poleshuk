# Проектирование базы данных: Ветеринарная клиника

## 1. Сущности и атрибуты

В базе данных выделены четыре основные сущности:

### `doctors`
Хранит информацию о ветеринарах.

Атрибуты:
- `doctor_id`
- `first_name`
- `last_name`
- `specialty`

### `owners`
Хранит информацию о владельцах питомцев.

Атрибуты:
- `owner_id`
- `first_name`
- `last_name`
- `phone_number`

### `pets`
Хранит информацию о питомцах и связывает каждого питомца с его владельцем.

Атрибуты:
- `pet_id`
- `pet_name`
- `owner_id`

### `visits`
Хранит информацию о приёмах в клинике

Атрибуты:
- `visit_id`
- `doctor_id`
- `pet_id`
- `visit_type`
- `complaints`
- `diagnosis`
- `visit_date`

---

# 2. Проектирование таблиц

## Table Name: `doctors`

**Description:** Таблица хранит информацию о ветеринарах.

### Attributes

- `doctor_id`: UUID, PK
- `first_name`: VARCHAR(50), NOT NULL
- `last_name`: VARCHAR(50), NOT NULL
- `specialty`: VARCHAR(100), NOT NULL

### Constraints

- `pk_doctors`: PRIMARY KEY (`doctor_id`)
- `chk_doctors_specialty`: CHECK (`specialty` IN (
        'Surgeon',
        'Dermatologist',
        'Cardiologist',
        'Oncologist'
    ))

---

## Table Name: `owners`

**Description:** Таблица хранит информацию о владельцах питомцев.

### Attributes

- `owner_id`: UUID, PK
- `first_name`: VARCHAR(50), NOT NULL
- `last_name`: VARCHAR(50), NOT NULL
- `phone_number`: VARCHAR(20), NOT NULL, UNIQUE

### Constraints

- `pk_owners`: PRIMARY KEY (`owner_id`)
- `uq_owners_phone_number`: UNIQUE (`phone_number`)

---

## Table Name: `pets`

**Description:** Таблица хранит информацию о питомцах. Каждый питомец связан с одним владельцем через внешний ключ `owner_id`.

### Attributes

- `pet_id`: UUID, PK
- `pet_name`: VARCHAR(50), NOT NULL
- `owner_id`: UUID, FK (REFERENCES `owners`), NOT NULL

### Constraints

- `pk_pets`: PRIMARY KEY (`pet_id`)
- `fk_pets_owners`: FOREIGN KEY (`owner_id`) REFERENCES `owners`(`owner_id`)

---

## Table Name: `visits`

**Description:** Таблица хранит информацию о приёмах питомцев у ветеринарных врачей. Через неё реализуется связь «многие-ко-многим» между таблицами `doctors` и `pets`.

### Attributes

- `visit_id`: UUID, PK
- `doctor_id`: UUID, FK (REFERENCES `doctors`), NOT NULL
- `pet_id`: UUID, FK (REFERENCES `pets`), NOT NULL
- `visit_type`: VARCHAR(50), NOT NULL
- `complaints`: TEXT
- `diagnosis`: TEXT
- `visit_date`: DATE, NOT NULL, DEFAULT CURRENT_DATE

### Constraints

- `pk_visits`: PRIMARY KEY (`visit_id`)
- `fk_visits_doctors`: FOREIGN KEY (`doctor_id`) REFERENCES `doctors`(`doctor_id`)
- `fk_visits_pets`: FOREIGN KEY (`pet_id`) REFERENCES `pets`(`pet_id`)
- `chk_visits_type`: CHECK (`visit_type` IN ('consultation', 'vaccination', 'surgery', 'checkup'))

---

# 3. Взаимосвязи между таблицами

## `owners` и `pets` — Один-ко-Многим (1:N)

Один владелец может иметь несколько питомцев, но каждый питомец относится к одному владельцу.

Внешний ключ:

`pets.owner_id` → `owners.owner_id`

---

## `doctors` и `visits` — Один-ко-Многим (1:N)

Один ветеринарный врач может провести множество приёмов, но каждая запись о приёме относится к одному врачу.

Внешний ключ:

`visits.doctor_id` → `doctors.doctor_id`

---

## `pets` и `visits` — Один-ко-Многим (1:N)

Один питомец может иметь множество приёмов, но каждая запись в таблице `visits` относится к одному конкретному питомцу.

Внешний ключ:

`visits.pet_id` → `pets.pet_id`

---

## `doctors` и `pets` — Многие-ко-Многим (M:N)

Один врач может принимать множество разных питомцев, а один питомец в течение времени может посещать разных врачей.

Связь «многие-ко-многим» реализуется через промежуточную таблицу `visits`:

`doctors` → `visits` ← `pets`

Для реализации используются два внешних ключа:

- `visits.doctor_id` → `doctors.doctor_id`
- `visits.pet_id` → `pets.pet_id`