#!/usr/bin/env python3

# import time, os and clear screen
import os
import time

os.system("clear")

print("")
print("               -s-                                                                   ")
print("               odo`      -+-`                                                        ")
print("              `yhh.  .  -hdh+`                                                       ")
print("              .y+.`-:.  oddyh/      ______                _     ___  ___      _ _    ")
print("     .        .. .//.   /ddhys.     | ___ \              (_)    |  \/  |     (_) |   ")
print("    --          `///`    -oyhy.     | |_/ /_      ___ __  _  ___| .  . | __ _ _| |   ")
print("   .y++-+/`./+/:::::.      `/+`     |  __/\ \ /\ / / '_ \| |/ _ \ |\/| |/ _` | | |   ")
print("   .os/h- -Noyddhhhs:hy:.y:oo.      | |    \ V  V /| | | | |  __/ |  | | (_| | | |   ")
print("    `/do  .hN+ddddd:.dMN`yd+`       \_|     \_/\_/ |_| |_|_|\___\_|  |_/\__,_|_|_|   ")
print("     .ho  -/.-ddddd.:/:/ sh.                                                         ")
print("     `+mo:   .dhhhd.   -+m+`                                                         ")
print("      :dm+-.-ohhhhh+.``/md:                                                          ")
print("      `/hdhhhhyhdhsdhhhdh+`                              			    ")
print("        -ohddh:.--+dddhs:                              			            ")
print("         `.+hdy///hdh+-`              ``.-----..`    			            ")
print("           `sddhhhds:              `.---.....-:/:-       			    ")
print("           .ydddddy   .` `...``  `..``         `:/:`      			    ")
print("           +dddddds  `: +yhhhyy+:.               :/:  			            ")
print("          .yddddddy `:.`hddddddhho.              `//`    		            ")
print("          .hddddddd---`sdddddddhooo`              //.   			            ")
print("          .ydddddddy:`odddddddddyoh-              //-    			    ")
print("          `oddddddddhydddddydddddyd:             `//-    			    ")
print("         `.:shdddddddddddddyydddddh-             -//.  			            ")
print("        -oooooshhhhdddyddhhhoshdddy.             ///`  			            ")
print("        /sssssooo+sdddyo+/oosooyddh+:`          -///  			            ")
print("        /ssso/--..odddd+``+ssss+yddddo`        `///-     			    ")
print("        :sssss+:` oddddh- :sssss/hddddo`       :///`  			            ")
print("        .ossssss- oddddd+ -sssss//dddddo`     -///:   			            ")
print("         -osssss-`oddddds./sssss+.yddddh/    -///:`   			            ")
print("          ./oss+``sdddddh:+sssss/`+dddddy.  .:-.`   			            ")
print("            .:-` .ydddddd/ssssss: /dddddh.         			            ")
print("                 :hdddddd+ssssso- +dddddhs.     			                    ")
print("                `sddddddd+sssso: .yddddddh-      			            ")
print("               `+dddddddh:....`  :yyhhhhyo.        			            ")
print("               `+syyyyso:`         ``````        			            ")
print("           								       	    ")
print("          					          	                    ")
print("")




# Import required Modules
# They can be found at:
# https://github.com/berend/haveibeenpwnd
# http://zetcode.com/python/prettytable/
from haveibeenpwnd import check_email
from prettytable import PrettyTable



# Import an email list from a txt file.
textFile = input("Please select a list of email addresses to import: ")


# Import the textFile and split it up
# into individual lines.
with open(textFile) as eMail_list:
        for line in eMail_list:
            for eMailAddress in line.split():
                emails = [str(eMailAddress)]


                # Create a function that will test each email on the list
                # against the haveibeenpwnd database
                # strip extra spaces and make all lowercase
                def view_status(words):
                    for eMailAddress in emails:
                        addresses = (eMailAddress.lower()); addresses = (addresses.strip())

                        # this will create a variable in the python dictionary list
                        # and strip "breaches"
                        tempOut = check_email(addresses)
                        query = tempOut["breaches"]
                        # Rate limit 2 seconds per query
                        time.sleep(2)
                        print("")


                        # inform user of pwnage found by the numbers
                        timesPwnd = len(query)
                        if timesPwnd < 1:
                            print(f"Dang. You're lucky. No pwnage found for {addresses}!")
                        elif timesPwnd > 10:
                            print(f"Holy crap! Your email ({addresses}) has been pwnd {timesPwnd} times. Hope you're not on Ashley Madison!")
                        else:
                            print(f"Pwn records found for {addresses}: {timesPwnd}.")

                        # assign a variable to our table
                        x = PrettyTable()

                        breach_list = {}

                        i = 0

                        # Print names for each breach
                        for item in query:

                            x.field_names = ["Email", "Name", "Domain", "BreachDate", "AddedDate", "Pwn Count", "Type of data released", "Is a Spam List"]
                            Name = item["Name"]
                            Domain = item["Domain"]
                            BreachDate = item["BreachDate"]
                            AddedDate = item["AddedDate"]
                            PwnCount = "{:,}".format(item["PwnCount"])
                            DataClasses = str(item["DataClasses"])
                            IsSpamList = str(item["IsSpamList"])


                            x.add_row([addresses, Name, Domain, BreachDate, AddedDate, PwnCount, DataClasses, IsSpamList])



                        print (x)


                view_status(emails)
