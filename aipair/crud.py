import os
import sqlite3
from typing import Any, Dict, List, Optional

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "courses.db")
TABLE_NAME = "COURSES"


def _get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def _ensure_table_exists(connection: sqlite3.Connection) -> None:
    connection.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            duration REAL NOT NULL,
            fee REAL NOT NULL
        )
        """
    )
    connection.commit()


def _validate_course_id(course_id: Any) -> int:
    if course_id is None:
        raise ValueError("Course id is required.")
    if isinstance(course_id, bool) or not isinstance(course_id, int):
        raise ValueError("Course id must be an integer.")
    if course_id <= 0:
        raise ValueError("Course id must be a positive integer.")
    return course_id


def _validate_title(title: Any) -> str:
    if not isinstance(title, str):
        raise ValueError("Course title must be a string.")
    normalized = title.strip()
    if not normalized:
        raise ValueError("Course title must not be empty.")
    return normalized


def _validate_duration(duration: Any) -> float:
    if isinstance(duration, bool):
        raise ValueError("Course duration must be a numeric value.")
    if not isinstance(duration, (int, float)):
        raise ValueError("Course duration must be a numeric value.")
    if duration <= 0:
        raise ValueError("Course duration must be greater than zero.")
    return float(duration)


def _validate_fee(fee: Any) -> float:
    if isinstance(fee, bool):
        raise ValueError("Course fee must be a numeric value.")
    if not isinstance(fee, (int, float)):
        raise ValueError("Course fee must be a numeric value.")
    if fee < 0:
        raise ValueError("Course fee must be zero or a positive value.")
    return float(fee)


def _normalize_course_row(row: sqlite3.Row) -> Dict[str, Any]:
    return {
        "id": row["id"],
        "title": row["title"],
        "duration": row["duration"],
        "fee": row["fee"],
    }


def initialize_database() -> None:
    """Ensure the COURSES table exists in the database."""
    with _get_connection() as connection:
        _ensure_table_exists(connection)


def create_course(course_id: Any, title: Any, duration: Any, fee: Any) -> Dict[str, Any]:
    """Insert a new course into the database."""
    course_id = _validate_course_id(course_id)
    title = _validate_title(title)
    duration = _validate_duration(duration)
    fee = _validate_fee(fee)

    with _get_connection() as connection:
        _ensure_table_exists(connection)
        existing = connection.execute(
            f"SELECT 1 FROM {TABLE_NAME} WHERE id = ?",
            (course_id,),
        ).fetchone()
        if existing:
            raise ValueError(f"A course with id {course_id} already exists.")

        connection.execute(
            f"INSERT INTO {TABLE_NAME} (id, title, duration, fee) VALUES (?, ?, ?, ?)",
            (course_id, title, duration, fee),
        )
        connection.commit()

    return read_course(course_id)


def read_course(course_id: Any) -> Dict[str, Any]:
    """Return a single course by id."""
    course_id = _validate_course_id(course_id)

    with _get_connection() as connection:
        _ensure_table_exists(connection)
        row = connection.execute(
            f"SELECT * FROM {TABLE_NAME} WHERE id = ?",
            (course_id,),
        ).fetchone()

    if row is None:
        raise ValueError(f"Course with id {course_id} not found.")

    return _normalize_course_row(row)


def read_all_courses() -> List[Dict[str, Any]]:
    """Return all courses from the database."""
    with _get_connection() as connection:
        _ensure_table_exists(connection)
        rows = connection.execute(
            f"SELECT * FROM {TABLE_NAME} ORDER BY id").fetchall()

    return [_normalize_course_row(row) for row in rows]


def update_course(
    course_id: Any,
    title: Optional[Any] = None,
    duration: Optional[Any] = None,
    fee: Optional[Any] = None,
) -> Dict[str, Any]:
    """Update one or more fields on an existing course."""
    course_id = _validate_course_id(course_id)

    updates = []
    parameters: List[Any] = []

    if title is not None:
        updates.append("title = ?")
        parameters.append(_validate_title(title))
    if duration is not None:
        updates.append("duration = ?")
        parameters.append(_validate_duration(duration))
    if fee is not None:
        updates.append("fee = ?")
        parameters.append(_validate_fee(fee))

    if not updates:
        raise ValueError(
            "At least one field (title, duration, fee) must be provided to update.")

    parameters.append(course_id)

    with _get_connection() as connection:
        _ensure_table_exists(connection)
        cursor = connection.execute(
            f"UPDATE {TABLE_NAME} SET {', '.join(updates)} WHERE id = ?",
            tuple(parameters),
        )
        if cursor.rowcount == 0:
            raise ValueError(f"Course with id {course_id} not found.")
        connection.commit()

    return read_course(course_id)


def delete_course(course_id: Any) -> None:
    """Delete a course by id."""
    course_id = _validate_course_id(course_id)

    with _get_connection() as connection:
        _ensure_table_exists(connection)
        cursor = connection.execute(
            f"DELETE FROM {TABLE_NAME} WHERE id = ?",
            (course_id,),
        )
        if cursor.rowcount == 0:
            raise ValueError(f"Course with id {course_id} not found.")
        connection.commit()
