# Проектирование базы данных: Ветеринарная клиника

## 1. Сущности и атрибуты

В базе данных выделены семь основных сущностей:

### `doctors`
Хранит информацию о ветеринарах.

Атрибуты:
- `doctor_id`
- `first_name`
- `last_name`

### `specialties_ref`
Хранит список доступных специализаций врачей.

Атрибуты:
- `specialty_id`
- `specialty_name`

### `doctor_specialties`
Связывает врачей с их специализациями.

Атрибуты:
- `doctor_id`
- `specialty_id`

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

### `visit_history`
Хранит информацию о запланированных приёмах в клинике.

Атрибуты:
- `visit_id`
- `doctor_id`
- `pet_id`
- `visit_type`
- `visit_timestamp`

### `visits`
Хранит медицинские записи по приёмам.

Атрибуты:
- `record_id`
- `visit_id`
- `complaints`
- `diagnosis`

---

# 2. Проектирование таблиц

## Table Name: `doctors`

**Description:** Таблица хранит информацию о ветеринарах.

### Attributes

- `doctor_id`: UUID, PK
- `first_name`: VARCHAR(50), NOT NULL
- `last_name`: VARCHAR(50), NOT NULL

### Constraints

- `pk_doctors`: PRIMARY KEY (`doctor_id`)

---

## Table Name: `specialties_ref`

**Description:** Справочная таблица со списком доступных специализаций врачей.

### Attributes

- `specialty_id`: UUID, PK
- `specialty_name`: VARCHAR(100), NOT NULL, UNIQUE

### Constraints

- `pk_specialties_ref`: PRIMARY KEY (`specialty_id`)
- `uq_specialties_ref_specialty_name`: UNIQUE (`specialty_name`)

---

## Table Name: `doctor_specialties`

**Description:** Промежуточная таблица для связи «многие-ко-многим» между врачами и специализациями.

### Attributes

- `doctor_id`: UUID, FK (REFERENCES `doctors`), NOT NULL
- `specialty_id`: UUID, FK (REFERENCES `specialties_ref`), NOT NULL

### Constraints

- `pk_doctor_specialties`: PRIMARY KEY (`doctor_id`, `specialty_id`)
- `fk_doctor_specialties_doctors`: FOREIGN KEY (`doctor_id`) REFERENCES `doctors`(`doctor_id`)
- `fk_doctor_specialties_specialties_ref`: FOREIGN KEY (`specialty_id`) REFERENCES `specialties_ref`(`specialty_id`)

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

## Table Name: `visit_history`

**Description:** Таблица хранит информацию о запланированных приёмах питомцев у ветеринарных врачей. Через неё реализуется связь «многие-ко-многим» между таблицами `doctors` и `pets`.

### Attributes

- `visit_id`: UUID, PK
- `doctor_id`: UUID, FK (REFERENCES `doctors`), NOT NULL
- `pet_id`: UUID, FK (REFERENCES `pets`), NOT NULL
- `visit_type`: VARCHAR(50), NOT NULL
- `visit_timestamp`: TIMESTAMP, NOT NULL

### Constraints

- `pk_visit_history`: PRIMARY KEY (`visit_id`)
- `fk_visit_history_doctors`: FOREIGN KEY (`doctor_id`) REFERENCES `doctors`(`doctor_id`)
- `fk_visit_history_pets`: FOREIGN KEY (`pet_id`) REFERENCES `pets`(`pet_id`)
- `chk_visit_history_type`: CHECK (`visit_type` IN ('consultation', 'vaccination', 'surgery', 'checkup'))

---

## Table Name: `visits`

**Description:** Таблица хранит медицинские записи, которые создаются по результатам приёмов.

### Attributes

- `record_id`: UUID, PK
- `visit_id`: UUID, FK (REFERENCES `visit_history`), NOT NULL
- `complaints`: TEXT
- `diagnosis`: TEXT

### Constraints

- `pk_visits`: PRIMARY KEY (`record_id`)
- `fk_visits_visit_history`: FOREIGN KEY (`visit_id`) REFERENCES `visit_history`(`visit_id`)

---

# 3. Взаимосвязи между таблицами

## `owners` и `pets` — Один-ко-Многим (1:N)

Один владелец может иметь несколько питомцев, но каждый питомец относится к одному владельцу.

Внешний ключ:

`pets.owner_id` → `owners.owner_id`

---

## `doctors` и `visit_history` — Один-ко-Многим (1:N)

Один ветеринарный врач может провести множество приёмов, но каждая запись о приёме относится к одному врачу.

Внешний ключ:

`visit_history.doctor_id` → `doctors.doctor_id`

---

## `pets` и `visit_history` — Один-ко-Многим (1:N)

Один питомец может иметь множество приёмов, но каждая запись в таблице `visit_history` относится к одному конкретному питомцу.

Внешний ключ:

`visit_history.pet_id` → `pets.pet_id`

---

## `visit_history` и `visits` — Один-ко-Многим (1:N)

Один приём может иметь несколько медицинских записей, но каждая медицинская запись относится к одному приёму.

Внешний ключ:

`visits.visit_id` → `visit_history.visit_id`

---

## `doctors` и `specialties_ref` — Многие-ко-Многим (M:N)

Один врач может иметь несколько специализаций, а одна специализация может быть у нескольких врачей.

Связь «многие-ко-многим» реализуется через промежуточную таблицу `doctor_specialties`:

`doctors` → `doctor_specialties` ← `specialties_ref`

Для реализации используются два внешних ключа:

- `doctor_specialties.doctor_id` → `doctors.doctor_id`
- `doctor_specialties.specialty_id` → `specialties_ref.specialty_id`

---

## `doctors` и `pets` — Многие-ко-Многим (M:N)

Один врач может принимать множество разных питомцев, а один питомец в течение времени может посещать разных врачей.

Связь «многие-ко-многим» реализуется через промежуточную таблицу `visit_history`:

`doctors` → `visit_history` ← `pets`

Для реализации используются два внешних ключа:

- `visit_history.doctor_id` → `doctors.doctor_id`
- `visit_history.pet_id` → `pets.pet_id`
