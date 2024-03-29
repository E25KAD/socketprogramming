Host : 127.0.0.1
Username : root
Password : root
Port : 21

Method 1 : Run On VS Code
1.กดรันไฟล์ myftp.py
2.พิมพ์ใน terminal หรือ cmd ว่า ftp> open 127.0.0.1 แล้วกด Enter
3.พิมพ์ username และ password ข้างต้น และระบบจะแสดงคำว่า 230 Login successful.
4.ทำการสร้างไฟล์ test.txt (โฟลเดอร์ ftp ชื่อว่า ftp_folder)
5.พิมพ์คำสั่ง put test.txt เพื่ออัปโหลดไฟล์ไปยัง ftp_folder ระบบจะโชว์ 226 Transfer complete.
ftp: 59 bytes received in 0.00Seconds 59000.00Kbytes/sec.

Method 2 : FileZilla
1.กรอกข้อความในช่อง
Host:127.0.0.1 ,Username:root ,Password:root ,Port:21 และกด Quick Connect
2.ทำการลากไฟล์หรือคลิ๊กขวาที่ไฟล์และเลือก Upload ไฟล์ที่เราต้องการในฝั่งซ้าย (Local Site) ระบบจะทำการอัพโหลดรอสักครู่แล้วเสร็จสิ้น