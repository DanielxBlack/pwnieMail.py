#!/usr/bin/env python3

# import os and clear screen
import os
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
from haveibeenpwnd import check_email
from prettytable import PrettyTable


# Ask for email address and assign a variable
# Strip spaces and make lowercase.
# eMailAddy = input("Enter an email address: ")
# eMailAddy = eMailAddy.strip()
# eMailAddy = eMailAddy.lower()


# Import an email list
textFile = input("Please select a list of email addresses to import: ")


with open(textFile) as eMail_list:
        for line in eMail_list:
            for eMailAddress in line.split():
                emails = [str(eMailAddress)]

                # def show_status and create a for loop
                # strip spaces and make all lowercase
                def view_status(words):
                    for eMailAddress in emails:
                        addresses = (eMailAddress.lower()); addresses = (addresses.strip())
                        #print(addresses)
                        tempOut = check_email(addresses)
                        query = tempOut["breaches"]
                        print("")
                        timesPwnd = len(query)
                        if timesPwnd < 1:
                            print("Dang. You're lucky. No pwnage found for {addresses}!")
                        elif timesPwnd > 10:
                            print(f"Holy crap! Your email ({addresses}) has been pwnd {timesPwnd} times. Hope you're not on Ashley Madison!")
                        else:
                            print(f"Pwn records found for {addresses}: {timesPwnd}.")

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
