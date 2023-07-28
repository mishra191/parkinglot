import unittest
from main.main import Main
from datetime import datetime

class MainTestCase(unittest.TestCase):
    
    def setUp(self):
      self.main_instance = Main()
     

    def test_reserveUnreserve1Parking(self):
      self.main_instance.run('rules2.json')  
      startTime = datetime(2023, 7, 17, 11, 30, 00) 
      parkingticket = self.main_instance.reserveParking(startTime, '0', 'NP')
      self.assertEqual(str(parkingticket), "Ticket Number: 001 2023-07-17 11:30:00, Parking Ticket: 001");
      outTime = datetime(2023, 7, 17, 12, 30, 00) 
      parkingReceipt =self.main_instance.unReserveParking(parkingticket, outTime);
      
      print('parkingReceipt', parkingReceipt)
      
      self.assertEqual(parkingReceipt.feeAmount, 10.0);
      
    def test_reserveUnreserve2Parking(self):
       self.main_instance.run('rules2.json')  
       startTime = datetime(2023, 7, 17, 11, 30, 00) 
       parkingticket = self.main_instance.reserveParking(startTime, '0', 'NP')
       self.assertEqual(str(parkingticket), "Ticket Number: 001 2023-07-17 11:30:00, Parking Ticket: 001");
       outTime = datetime(2023, 7, 17, 14, 30, 00) 
       parkingReceipt =self.main_instance.unReserveParking(parkingticket, outTime);
       
       print('parkingReceipt', parkingReceipt)
       
       self.assertEqual(parkingReceipt.feeAmount, 20.0);
       
    def test_reserveUnreserve3Parking(self):
         self.main_instance.run('rules2.json')  
         startTime = datetime(2023, 7, 17, 11, 30, 00) 
         parkingticket = self.main_instance.reserveParking(startTime, '0', 'NP')
         self.assertEqual(str(parkingticket), "Ticket Number: 001 2023-07-17 11:30:00, Parking Ticket: 001");
         outTime = datetime(2023, 7, 17, 15, 30, 00) 
         parkingReceipt =self.main_instance.unReserveParking(parkingticket, outTime);
         
         print('parkingReceipt', parkingReceipt)
         
         self.assertEqual(parkingReceipt.feeAmount, 30.0);
      
   
              
            
if __name__ == '__main__':
    unittest.main()


