#Task 1
### 1.1
### Present the structure of a program consist of elementary components and composite components.

### 1.2
### '*' means in the corner of components that are repeated. '。' means selection between 2 components.

### 1.3
WHILE ____?
	CALL ReadSalary()
	IF Salary > 50
	THEN
		IF Salary >= 90
		THEN
			Role <- Assign Project Manager
		ELSE
			Role <- Assign Lead Developer
		ENDIF
	ELSE
		Role <- Manger
	ENDIF
ENDWHILE

### 1.4
https://github.com/DennisZhang246/2017A2CS/blob/master/Pre-release/Task%201.4.jpeg


### 1.5
WHILE ____?
	CALL ReadSalary()
	IF Salary > 50
	THEN
		IF Salary > 70
		THEN
			IF Salary >=90
				Role <- Assign Project Manager
			ELSE
				Role <- Consultant
			ENDIF
		ELSE
			Role <- Assign Lead Developer
		ENDIF
	ELSE
		Role <- Manager
ENDWHILE

### 1.6
def IdentifyRole(role):
    if salary>50:
        if salary>70:
            if salary>=90
                return 'projectmanager'
            else:
                return 'consultant'
        else:
            return 'leaddeveloper'
    else:
        return 'manager'
