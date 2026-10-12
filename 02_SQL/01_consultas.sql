-- LABORATORIO 2: POSTGRESQL
-- Análisis de empleados

-- 1. Consultar todos los registros
SELECT *
FROM empleados;

-- 2. Calcular estadísticas por departamento
SELECT
    departamento,
    COUNT(*) AS total_empleados,
    ROUND(AVG(sueldo), 2) AS sueldo_promedio,
    MAX(sueldo) AS sueldo_maximo,
    MIN(sueldo) AS sueldo_minimo
FROM empleados
GROUP BY departamento
ORDER BY sueldo_promedio DESC;