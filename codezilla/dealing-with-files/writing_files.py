'''
                  |  r  r+  w  w+  a  a+
__________________|_____________________
read              |  +  +      +       +    
write             |     +   +  +   +   +
create            |         +  +   +   +    making new file
truncate          |         +  +            deleting what in the file      
position at start |  +  +   +  +
position at end   |                +   +
'''

# r
# لو عايز تقرأ بس

# w
# لو عايز تكتب بس بمعني إنك هتمسح الفايل وتكتب فيه من الأول

# a
# لو عايز تكتب بمعني إنك هتضيف حاجه علي آخر الفايل

# لو عايز قرأ وتكتب

# w+
# هتقرأ تكتب بس بشرط هتسمح كل حاجه وتكتب من الأول

# r+
# هتقرأ وتكتب فنفس الفايل من غير ما يتمسح ولكن من أول سطر

# a+
# هتقرأ وتكتب ولكن من آخر السطر

workers_file = open("My_file.text", "a")
workers_file.write("\n omar is a teacher ")
# هيطبع علي حسب مكان الكيرسر
# وممكن أتجنب أنه يطبع جنب آخر سطر ممكن أكتب \n


workers_file.close()
