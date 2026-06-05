# Pipeline Databases - AI Academy (DLH)

![SQL](https://img.shields.io/badge/SQL-MySQL-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-Shell%20%26%20PyMongo-green)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project contains SQL, MongoDB shell, and PyMongo exercises for database fundamentals. It covers database creation, table manipulation, querying, joins, aggregation, indexes, triggers, stored procedures, views, functions, and document operations.

---

## Objective

To strengthen database and data pipeline skills by learning:

- MySQL database and table creation
- SQL filtering, sorting, joins, and aggregation
- SQL constraints and `ENUM` values
- Indexes, views, triggers, stored procedures, and functions
- MongoDB shell commands
- MongoDB CRUD operations
- PyMongo collection operations
- Log statistics and aggregation queries
- Weighted average calculations

---

## Topics Covered

### MySQL

- Creating databases and tables
- Inserting and selecting rows
- Filtering and ordering query results
- Aggregate functions
- Grouping data
- Inner and left joins
- Unique constraints
- `ENUM` fields
- Index optimization
- Views
- Triggers
- Stored procedures
- SQL functions

### MongoDB Shell

- Listing databases
- Creating or switching databases
- Inserting documents
- Finding documents
- Counting documents
- Updating documents
- Deleting documents
- Regex queries

### MongoDB with Python

- Listing collection documents
- Inserting documents with PyMongo
- Updating nested document fields
- Filtering documents by topic
- Aggregating scores
- Computing log statistics
- Ranking top IP addresses

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- MySQL
- MongoDB
- PyMongo
- `pycodestyle` 2.11.1
- Python files should be executable
- Python files should begin with `#!/usr/bin/env python3`
- SQL files should be executable in MySQL-compatible environments

---

## Files

### MySQL Basics and Queries

| File | Description |
| --- | --- |
| `0-create_database_if_missing.sql` | Creates database `db_0` if it does not exist |
| `1-first_table.sql` | Creates `first_table` with `id` and `name` columns |
| `2-list_values.sql` | Lists all rows from `first_table` |
| `3-insert_value.sql` | Inserts a row into `first_table` |
| `4-best_score.sql` | Lists records with score greater than or equal to 10 |
| `5-average.sql` | Computes the average score |
| `6-avg_temperatures.sql` | Displays average temperature by city |
| `7-max_state.sql` | Displays maximum temperature by state |
| `8-genre_id_by_show.sql` | Lists shows linked to at least one genre |
| `9-no_genre.sql` | Lists shows without a linked genre |
| `10-count_shows_by_genre.sql` | Counts shows by genre |
| `11-rating_shows.sql` | Lists shows by total rating |
| `12-rating_genres.sql` | Lists genres by total rating |

### MySQL Constraints and Advanced Features

| File | Description |
| --- | --- |
| `13-uniq_users.sql` | Creates a `users` table with unique email addresses |
| `14-country_users.sql` | Creates a `users` table with a country `ENUM` |
| `15-fans.sql` | Ranks band origins by number of fans |
| `16-glam_rock.sql` | Lists Glam rock bands by lifespan |
| `17-store.sql` | Creates a trigger to decrease item quantity after orders |
| `18-valid_email.sql` | Creates a trigger to reset email validity when email changes |
| `19-bonus.sql` | Creates `AddBonus` stored procedure |
| `20-average_score.sql` | Creates procedure to compute average score for a user |
| `21-div.sql` | Creates `SafeDiv` SQL function |
| `21-init.sql` | Initializes sample data for division tasks |
| `100-index_my_names.sql` | Creates an index on the first letter of `name` |
| `101-index_name_score.sql` | Creates an index on first letter of `name` and `score` |
| `102-need_meeting.sql` | Creates a view for students needing a meeting |
| `103-average_weighted_score.sql` | Creates procedure for weighted average scores |

### MongoDB Shell

| File | Description |
| --- | --- |
| `22-list_databases` | Lists MongoDB databases |
| `23-use_or_create_database` | Uses or creates `my_db` |
| `24-insert` | Inserts a school document |
| `25-all` | Lists all school documents |
| `26-match` | Finds schools by exact name |
| `27-count` | Counts school documents |
| `28-update` | Updates matching school documents with an address |
| `29-delete` | Deletes matching school documents |
| `104-find` | Finds school documents with names beginning with `Holberton` |

### PyMongo

| File | Description |
| --- | --- |
| `30-all.py` | Lists all documents in a collection |
| `31-insert_school.py` | Inserts a school document and returns its `_id` |
| `32-update_topics.py` | Updates topics for all schools matching a name |
| `33-schools_by_topic.py` | Finds schools that include a specific topic |
| `34-log_stats.py` | Prints Nginx log statistics by method and status path |
| `105-students.py` | Returns students sorted by average topic score |
| `106-log_stats.py` | Prints Nginx log statistics and top IP addresses |

---

## Usage

Run a MySQL script:

```bash
mysql -uroot -p < 0-create_database_if_missing.sql
```

Run a MongoDB shell script:

```bash
mongo < 25-all
```

Run a PyMongo script:

```bash
python3 34-log_stats.py
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
