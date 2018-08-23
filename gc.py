
from __future__ import print_function
import gedcom
from colorama import Fore, Style, Back

gedcomfile = gedcom.parse("my.ged")

color_stages = [
        Fore.RED  + Style.DIM,
        Fore.GREEN+ Style.DIM, 
        Fore.YELLOW+ Style.DIM, 
        Fore.MAGENTA+ Style.DIM, 
        Fore.CYAN+ Style.DIM, 
        Fore.WHITE+ Style.DIM,
        Fore.RED,
        Fore.GREEN, 
        Fore.YELLOW, 
        Fore.MAGENTA, 
        Fore.CYAN, 
        Fore.WHITE,
        Fore.RED + Style.BRIGHT,
        Fore.GREEN + Style.BRIGHT,
        Fore.YELLOW+ Style.BRIGHT , 
        Fore.MAGENTA+ Style.BRIGHT, 
        Fore.CYAN+ Style.BRIGHT, 
        Fore.WHITE+ Style.BRIGHT,
        ]

generations = [0]*100

def tree(person, indent=0, silent=False):
    if not silent:
        print(indent*' '+ color_stages[indent] + ' '.join(person.name) + Style.RESET_ALL)
    generations[indent]+=1;
    indent += 1
    if person.mother is not None:
        tree(person.mother, indent, silent)
    if person.father is not None:
        tree(person.father, indent, silent)

def achievement(gen):
    for i, g in enumerate(gen):
        if g == 0:
            break
        max_g = 2**i
        if max_g == g:
            print(Fore.YELLOW+ Style.BRIGHT + "Generation "+str(i)+": " + str(g) + "/" + str(max_g) + Style.RESET_ALL)
        else:
            print("Generation "+str(i)+": " + str(g) + "/" + str(max_g))

def strmask(first_list, second_list):
    result = []
    for first, second in first_list, second_list:
        f = list(first)
        s = list(second)

        print(len(f), (len(s)))

        for x in range(len(f)):
            print("'",f[x], s[x], "'")
            f[x] = f[x] if f[x] > s[x] else s[x]

        first = ''.join(f)
        result.append(first)
    return result

# def graph(person, max_generation, cur_line="", stop_after=0, current=0):
#     # print("Line size: ", max_generation, current, max_generation*(2**current))


#     if current > stop_after:        
#         return ["", []]

#     cur_line = " "*max_generation
#     cur_list = list(cur_line)
    
#     # print("Color in item:", max_generation, max_generation//2, len(cur_list))
#     cur_list[max_generation//2] = person.name[1][0]
#     cur_line = ''.join(cur_list)

#     # else:
#     if person.mother is not None and current < stop_after:
#         mother_out, m_trail = graph(person.mother, max_generation/2 ,current=current+1, stop_after=stop_after)
#     else:
#         mother_out = Fore.CYAN+Style.DIM+"M"*(max_generation/2)+Style.RESET_ALL 
#         m_trail = []

#         # m_trail = []
#         # mother_out=''
#         t = stop_after-current       
#         c= 1
#         print("Generations left to fill:", t)
#         print("current Generations to pop:", c)
#         while c < t-1:
#             if c == 1:
#                 mother_out = ""
#             mother_out += Fore.CYAN+ "m"*(max_generation/(2*(c))) + Style.RESET_ALL
#             m_trail += [Fore.CYAN+Style.BRIGHT + "^^"*(max_generation/(2*(c))) + Style.RESET_ALL]
#             c+=1

#     if person.father is not None and current < stop_after:
#         father_out, f_trail = graph(person.father, max_generation/2 ,current=current+1, stop_after=stop_after)
#     else:
#         father_out = Fore.RED+Style.DIM+"F"*((max_generation)/2)+Style.RESET_ALL
#         # f_trail =[]

#         f_trail = []
#         father_out=''
#         t = stop_after-current       
#         c= 1
#         print(c,t)
#         while c < t-1:
#             if c == 1:
#                 father_out = ""
#             father_out += Fore.RED+"f"*(max_generation/(2*(c)))+Style.RESET_ALL
#             f_trail += [Fore.RED+Style.BRIGHT + "vv"*(max_generation/(2*(c)))+Style.RESET_ALL]
#             c+=1

#     next_line = [father_out + mother_out]
#     trail = f_trail + m_trail

#     if trail != '':
#         next_line.append(trail)

#     return [cur_line, next_line]    

me = gedcomfile.individuals.next()


tree(me, silent=True)
achievement(generations)
print("-----------------------------")
tree(me, silent=False)

# print()
# max_generation = 2**([idx for idx, x in enumerate(generations) if x == 0 ][0]-1)

# lim = 7
# max_generation = 2**(lim)

# a, b = graph(me, max_generation, stop_after=lim)


# def print_trail(trail):
#     next_gen = []
#     cur_line = []
#     for x in trail:
#         if type(x) == str and x != '':
#             cur_line += x
#         elif type(x) == list:
#             # print("_")
#             next_gen.extend(x)

#         else:
#             # print("")
#             pass
    
#     if len(cur_line) != 0: 
#         popped = ''.join(cur_line).replace(".", "")
#         if len(list(popped)) != 0:
#             print('|', ''.join(cur_line), '|')

#     if len(next_gen) != 0:
#         # print(len(next_gen) , "left: ", next_gen)
#         print_trail(next_gen)

# # print("B:", b)
# print('|',a,'|')
# print_trail(b)
