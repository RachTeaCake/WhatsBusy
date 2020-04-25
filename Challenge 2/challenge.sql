SELECT
  e.first_name AS e_first_name,
  e.last_name  AS e_last_name,
  m.first_name AS m_first_name,
  m.last_name  AS m_last_name
FROM table_1 t
LEFT JOIN employee e ON e.id_employee = t.id_employee
LEFT JOIN manager m ON m.id_manager = t.id_manager
WHERE dt_work_from >= '2020-01-01' AND dt_work_to <= '2020-01-31';
