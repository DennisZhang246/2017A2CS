#S3C3 Dennis Zhang S3C4 Michael Duan
#AccelerRead

import time
import random
import datetime

def start():
    print('')
    a=int(input('Command List: Type 1 to TEST reading speed; Type 2 to PRACTICE reading skill; Type 3 to QUIT.'))
    if a==1:
        test()
    elif a==2:
        practice()
    elif a==3:
        print('ByeBye!')
        quit()
    else:
        print('Invalid Command')
        start()

def test():
    global text
    a=0
    while a!=1:
        a=int(input('Type in 1 to start.When finishing reading,type in 2.'))
        if a==1:
            print('Ready?')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(0.5)
            print('GO!')
            start=datetime.datetime.now()
            print(testtext)
            b=0
            while b!=2:
                b=int(input())
                if b==2:
                    end=datetime.datetime.now()
                    print('You spent',(end-start),'seconds.')
                    timelength=(end-start).seconds
                    print(timelength)
                    print('Your reading speed is',281*60/timelength,'words per minute.')
                    print('')
                    practice()
        
def practice():
    global text
    print('This is Practice mode.Try to follow the passage appeared.')
    level=0
    while level<1 or level>5:
        level=int(input('Choose a level from 1 to 5.Level 5 is the hardest.'))
    print('You chosed Level',level,'.')
    a=0
    while a!=1:
        a=int(input('Type in 1 to start'))
        if a==1:
            print('Ready?')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(0.5)
            print('GO!')
            for i in range(1,10):
                print(text[i])
                time.sleep(7.2/level)
            b=str(input('Press A to practice again.Press any other button to go back.'))
            if b=='A':
                practice()
            else:
                start()

            
def main():
    print('Welcome to AccelerRead!')
    print('This programs aims at testing and improving your reading speed.')
    start()

text=['']*11
text[1]=['“Well, lots of people recognize that as humans get older they tend to have less and less children...trees do it the other way around.”']
text[2]=['David Lindenmayer. He studies conservation, landscape ecology and biodiversity at the Australian National University College of Science in Canberra.']
text[3]=['On January 26th he spoke to Scientific American Editor in Chief Mariette DiChristina when they were both at the World Economic Forum in Davos.']
text[4]=['DL: “What happens is that the older some of these really big old trees get, the more seeds they produce and the more germinants they’re likely to have. So it’s actually the polar opposite of what we see with humans and most other animals, so really quite extraordinary.”']
text[5]=['And how about the number of older trees that we have today, how does that look?']
text[6]=['“It’s quite a distressing situation, because in many, many forests and woodland and other ecosystems around the world, populations of large old trees are declining very, very quickly. ']
text[7]=['And this matters because a lot of biodiversity, a lot of carbon, a lot of key ecosystem processes are associated with those really big, old trees.']
text[8]=['Is there something we can do about this?Absolutely there is.']
text[9]=['We can make sure we grow more forest, we can make sure we protect the big trees that we have now, and we can make sure that we don’t do things that really put a lot of pressure on those trees.']
text[10]=['Straight out, just cutting them down—we should not be cutting down really big, old trees anymore.']

testtext=['The sea otter is a small mammal that lives in waters along the western coast of North America from California to Alaska. When some sea otter populations off the Alaskan coast started rapidly declining a few years ago, it caused much concern because sea otters play an important ecological role in the coastal ecosystem.',\
          'Experts started investigating the cause of the decline and quickly realized that there were two possible explanations: environmental pollution or attacks by predators. Initially, the pollution hypothesis seemed the more likely of the two.',\
          'The first reason why pollution seemed the more likely cause was that there were known sources of it along the Alaskan coast, such as oil rigs and other sources of industrial chemical pollution. Water samples from the area revealed increased levels of chemicals that could decrease the otters resistance to life-threatening infections and thus could indirectly cause their deaths.',\
          'Second, other sea mammals such as seals and sea lions along the Alaskan coast were also declining, indicating that whatever had endangered the otters was affecting other sea mammals as well. This fact again pointed to environmental pollution, since it usually affects the entire ecosystem rather than a single species.',\
          'Only widely occurring predators, such as the orca (a large predatory whale), could have the same effect, but orcas prefer to hunt much larger prey, such as other whales.',\
          'Third, scientists believed that the pollution hypothesis could also explain the uneven pattern of otter decline: at some Alaskan locations the otter populations declined greatly, while at others they remained stable. Some experts explained these observations by suggesting that ocean currents or other environmental factors may have created uneven concentrations of pollutants along the coast.']




main()

