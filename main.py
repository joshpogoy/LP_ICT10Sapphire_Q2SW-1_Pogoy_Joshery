from pyscript import document

def candidate_checker(e):
    club_members = ['Karlo Domingo', 'John Doe', 'Ryan Dye', 'Aaron Guzman', 'Yohan Kim', 'Max Calata', 'Sarah Connor', 'Tom Hanks', 'Emma Watson', 'Robert Downey', 'Chris Pratt', 'Jack Black', 'Brad Pitt', 'Tom Holland', 'Tom Cruise']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.',
                f'Congratulations {candidate}, your name is on the list!')

    document.getElementById('result').innerHTML = messages[member_checker]