---
title: "Pie Board"
author: "SbRhubarbPie"
description: "A custom 100% keyboard"
created_at: "2025-05-23"
---

# May 23, 2025
  Started going through lots of videos and threads to find ideas for parts and general ideas of what I might want to do for design. I found some cool keycaps that look like a sunset, and based on the color of RGB blacklighting they can look interesting.

![71nxtxnoUIL _AC_SL1500_](https://github.com/user-attachments/assets/9ab4c8ae-8bda-4039-9621-dc6d343a77a8)

 Found and went with what are supposedly one of the best budget linear switches (Gateron Milky Yellow), as well as decided on going for a 100% keyboard even if it may be more challenging because I like my numpad.
  
  **Total time spent today: 3hr**

# May 24, 2025
  Started going through tutorials and threads to find a suitable micro controller. I ended up going into a rabbit hole on directly soldering the chip onto the pcb and all the curcuits I would need for that. Althogh I learned a lot about this, I really just lack the experience and tools needed to directly solder a chip onto the PCB, so I decided on using a devboard. I ended up settling on the STM32F411 "blackpill" because I need an excessive amount of ports to handle a 100% keyboard matrix with RGB.

![image](https://github.com/user-attachments/assets/17639da7-7214-4ae0-8176-b91de63f6c0d)

I looked into the general design of keyboards to get an idea of how I would want to CAD the parts out to be printed in parts, which seems doable but will take some time.

![image](https://github.com/user-attachments/assets/67bed8d9-eced-435c-9918-a83b7569721f)

  **Total time spent today: 6hr**

# May 25, 2025
  I am revisiting what microcontroller to pick because the black pill is very expensive. I found the rp2350 stamp, which is really nice and I might go with instead, it is still a little expensive because of shipping but a lot better than the black pill.
  
![image](https://github.com/user-attachments/assets/5e597dac-7a56-464d-b6c7-48ea5171e471)


I have sunk a ton of time into the schematic and pcb design, I can tell this is gonna take a ton of revisions.

![image](https://github.com/user-attachments/assets/46e705bb-3e60-4e2c-9ff6-2ed007ed1c36)

![image](https://github.com/user-attachments/assets/5acebf7e-ab2f-44fb-a95a-a14bc5ba6f91)

Only partialy through the first routing but will 100% have to redo it at least a couple times

  **Total time spent today: 12hr**

# May 26, 2025
  I finished routing all of the adressable LEDs, then had to start rerouting all of them over again (twice) because I used the wrong footprints, which cost me a lot of time. I also researched data resistors for the LED strand which is very interesting and looked into usb c options abd routing.

  **Total time spent today: 7hr**

# May 27, 2025
  Added USB c, and an encoder, then researched and added a level shifter for my LED data line as well as making smaller changes and finishing routing.

  ![image](https://github.com/user-attachments/assets/011e30ae-d171-4e4c-8640-85a76201bff5)
  **Total time spent today: 4hr**

# May 28, 2025
  Fixed multiple small issues, implemented ground fills and did overall polish

  ![image](https://github.com/user-attachments/assets/431a338c-db5c-48eb-a8ec-489c70b10675)

  Researching how to implement fuse and ESD protection and starting work on the case
  **Total time spent today: 6hr**

# May 29, 2025
  Redid my routing again to implement a duplex switch matrix and added the ESD and fuse protection. Routed data lines as a differential pair once I realised it was important. I think I am mostly done with the PCB and will start to focus on the case.

  ![image](https://github.com/user-attachments/assets/4a93d954-404f-4187-840e-eb1cf6a391ef)

  ![image](https://github.com/user-attachments/assets/08aeceb4-62d9-4b19-b534-9ad90bc50cd0)

  ![image](https://github.com/user-attachments/assets/4606da61-9e26-4590-93d6-69ffa18ab279)

  ![image](https://github.com/user-attachments/assets/46b5c7c8-e4b2-4664-9024-0a4ef2ad39fe)

  **Total time spent today: 8hr**

# May 30, 2025
  Started building out the keyboard in fusion 360

  ![image](https://github.com/user-attachments/assets/e3576b7a-6dc0-4bc7-a072-e33d4489766d)

  ![image](https://github.com/user-attachments/assets/81ac7aa9-2fca-47a2-a12d-b633047fa953)

  **Total time spent today: 5hr**
