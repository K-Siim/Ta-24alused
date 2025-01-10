def calculate_bonus(employee):
    # Defineerime tulemuslikkuse hinnangute ja lisatasu protsentide seose
    performance_bonus = {
        1: 0,
        2: 0.05,
        3: 0.10,
        4: 0.15,
        5: 0.20
    }
    
    # Saame töötaja andmed
    name = employee['name']
    salary = employee['salary']
    performance = employee['performance']
    
    # Arvutame lisatasu
    bonus_percentage = performance_bonus.get(performance, 0)
    bonus = salary * bonus_percentage
    
    # Tagastame tulemuse
    return f"{name} lisatasu on: {bonus:.2f} eurot."

# Testimiseks
employee_data = {
    'name': 'Jaan',
    'salary': 3000,
    'performance': 4
}

print(calculate_bonus(employee_data))
