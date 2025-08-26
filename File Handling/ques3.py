#Write a program to generate multiplication tables from 2 to 20 and write it to the
#  desired files. Place these files in a folder
def generate_tables(n):
    content = ''
    for i in range(1,11):
        content += f"{n} x {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt", 'w') as f:
        f.write(content)


for i in range(2,21):
    generate_tables(i)