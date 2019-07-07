--1
SELECT employee.emp_no, employee.last_name, employee.first_name, employee.gender, salaries.salary
FROM employee
INNER JOIN salaries ON
employee.emp_no=salaries.emp_no;

--2
SELECT emp_no, last_name, first_name, hire_date
FROM employee
WHERE EXTRACT(year from hire_date) = 1986;

--3
SELECT dept_manager.dept_no, departments.dept_name, dept_manager.emp_no, employee.last_name, employee.first_name, dept_manager.from_date, dept_manager.to_date
FROM dept_manager 
INNER JOIN departments ON dept_manager.dept_no = departments.dept_no
INNER JOIN employee ON dept_manager.emp_no = employee.emp_no;

--4
SELECT dept_emp.emp_no, employee.last_name, employee.first_name, departments.dept_name
FROM dept_emp 
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
INNER JOIN employee ON dept_emp.emp_no = employee.emp_no;

--5
SELECT first_name, last_name
FROM employee
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

--6
SELECT dept_emp.emp_no, employee.last_name, employee.first_name, departments.dept_name
FROM dept_emp 
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
INNER JOIN employee ON dept_emp.emp_no = employee.emp_no
WHERE departments.dept_name = 'Sales'
;

--7
SELECT dept_emp.emp_no, employee.last_name, employee.first_name, departments.dept_name
FROM dept_emp 
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
INNER JOIN employee ON dept_emp.emp_no = employee.emp_no
WHERE departments.dept_name = 'Sales' OR departments.dept_name = 'Development'
;

--8
SELECT last_name, COUNT(last_name)
FROM employee
GROUP BY last_name
ORDER BY COUNT(last_name) DESC
;

