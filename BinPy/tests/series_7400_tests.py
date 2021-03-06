from BinPy.ic import *
from nose.tools import with_setup, nottest


def test_IC_7400():
    testIC = IC_7400()
    m = {1:1 ,2:0 ,4:1 ,5:1 ,7:0 ,9:0 ,10:1 ,12:0 ,13:0 ,14:1}
    testIC.setIC(m)
    n = {8: 1, 11: 1, 3: 1, 6: 0}
    if n != testIC.run():
        assert False
        
def test_IC_7401():        
    testIC = IC_7401()
    m = {2:1 ,3:0 ,5:1 ,6:1 ,7:0 ,8:0 ,9:1 ,11:0 ,12:0 ,14:1}        
    testIC.setIC(m)
    n = {1: 1, 4: 0, 10:1, 13: 1}
    if n != testIC.run():
        assert False

def test_IC_7402():        
    testIC = IC_7402()
    m = {2:1 ,3:0 ,5:1 ,6:1 ,7:0 ,8:0 ,9:1 ,11:0 ,12:0 ,14:1}        
    testIC.setIC(m)
    n = {1: 0, 10: 0, 4: 0, 13: 1}
    if n != testIC.run():
        assert False


def test_IC_7403():        
    testIC = IC_7403()
    m = {1:1 ,2:0 ,4:1 ,5:1 ,7:0 ,9:0 ,10:1 ,12:0 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = {8: 1, 11: 1, 3: 1, 6: 0}
    if n != testIC.run():
        assert False

def test_IC_7404():        
    testIC = IC_7404()
    m = {1:1 ,3:0 ,5:1 ,7:0, 9:0 ,11:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = {2: 0, 4: 1, 6: 0, 8: 1, 10: 0, 12: 1}
    if n != testIC.run():
        assert False
 
def test_IC_7405():        
    testIC = IC_7405()
    m = {1:1 ,3:0 ,5:1 ,7:0, 9:0 ,11:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = {2: 0, 4: 1, 6: 0, 8: 1, 10: 0, 12: 1}
    if n != testIC.run():
        assert False   
        
def test_IC_7408():        
    testIC = IC_7408()
    m = {1:1 ,2:0 ,4:0 ,5:1 ,7:0, 9:0 ,10:0 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n =  {8: 0, 11: 1, 3: 0, 6: 0}
    if n != testIC.run():
        assert False   
        
def test_IC_7410():        
    testIC = IC_7410()
    m = {1:1 ,2:0 ,13:0 ,3:1 ,4:1 ,5:0 ,7:0 ,9:0 ,10:0 ,11:1 ,14:1}        
    testIC.setIC(m)
    n =  {8: 1, 12: 1, 6: 1}
    if n != testIC.run():
        assert False  
        
def test_IC_7411():        
    testIC = IC_7411()
    m = {1:1 ,2:0 ,13:0 ,3:1 ,4:1 ,5:0 ,7:0 ,9:0 ,10:0 ,11:1 ,14:1}        
    testIC.setIC(m)
    n =  {8: 0, 12: 0, 6: 0}
    if n != testIC.run():
        assert False        
        
def test_IC_7412():        
    testIC = IC_7412()
    m = {1:1 ,2:0 ,13:0 ,3:1 ,4:1 ,5:0 ,7:0 ,9:0 ,10:0 ,11:1 ,14:1}        
    testIC.setIC(m)
    n =  {8: 1, 12: 1, 6: 1}
    if n != testIC.run():
        assert False
                
def test_IC_7413():        
    testIC = IC_7413()
    m = {1:1 ,2:0 ,4:0 ,5:1 ,7:0 ,9:0 ,10:0 ,12:0 ,13:0 ,14:1}        
    testIC.setIC(m)
    n =  {8: 1, 6: 1}
    if n != testIC.run():
        assert False        
        
def test_IC_7415():        
    testIC = IC_7415()
    m = {1:1 ,2:0 ,13:0 ,3:1 ,4:1 ,5:1 ,7:0 ,9:0 ,10:0 ,11:0 ,14:1}        
    testIC.setIC(m)
    n =  {8: 0, 12: 0, 6: 1}
    if n != testIC.run():
        assert False           

def test_IC_7416():        
    testIC = IC_7416()
    m = {1:1 ,3:0 ,5:0 ,7:0 ,9:1 ,11:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = {2: 0, 4: 1, 6: 1, 8: 0, 10: 0, 12: 1}
    if n != testIC.run():
        assert False 
        
def test_IC_7417():        
    testIC = IC_7417()
    m = {1:1 ,3:0 ,5:0 ,7:0 ,9:1 ,11:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = {2: 1, 4: 0, 6: 0, 8: 1, 10: 1, 12: 0}
    if n != testIC.run():
        assert False 
 
def test_IC_7418():        
    testIC = IC_7418()
    m = {1:1 ,2:0 ,4:1 ,5:0 ,7:0 ,9:1 ,10:1 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {8: 0, 6: 1}
    if n != testIC.run():
        assert False 

def test_IC_7419():        
    testIC = IC_7419()
    m = {1:1 ,3:1 ,5:1 ,7:0 ,9:1 ,11:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {2: 0, 4: 0, 6: 0, 8: 0, 10: 0, 12: 0}
    if n != testIC.run():
        assert False
        
def test_IC_7420():        
    testIC = IC_7420()
    m = {1:1 ,2:0 ,4:1 ,5:0 ,7:0 ,9:1 ,10:1 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {6: 1, 8: 0}
    if n != testIC.run():
        assert False 

def test_IC_7421():        
    testIC = IC_7421()
    m = {1:1 ,2:0 ,4:1 ,5:0 ,7:0 ,9:1 ,10:1 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {6: 0, 8: 1}
    if n != testIC.run():
        assert False                              
        
def test_IC_7422():        
    testIC = IC_7422()
    m = {1:1 ,2:0 ,4:1 ,5:0 ,7:0 ,9:1 ,10:1 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {6: 1, 8: 0}
    if n != testIC.run():
        assert False                                      
 
 
def test_IC_7424():        
    testIC = IC_7424()
    m = {1:1 ,2:0 ,4:1 ,5:0 ,7:0 ,9:0 ,10:0 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {8: 1, 11: 0, 3: 1, 6: 1}
    if n != testIC.run():
        assert False     
        
        
def test_IC_7425():        
    testIC = IC_7425()
    m = {1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,7:0 ,9:0 ,10:0 ,11:0 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {8: 0, 6: 1}
    if n != testIC.run():
        assert False                                                                       
        
        
def test_IC_7426():        
    testIC = IC_7426()
    m = {1:0 ,2:0 ,4:1 ,5:0 ,7:0 ,9:1 ,10:1 ,12:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = {3:1 ,6:1 ,8:0, 11:1}
    if n != testIC.run():
        assert False                  
  
  
  
def test_IC_7427():        
    testIC = IC_7427()
    m = {3:0 ,5:0 ,4:0 ,7:0 ,11:1 ,9:1 ,10:1 ,1:1 ,2:0 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = {6:1 ,8:0, 12:0}
    if n != testIC.run():
        assert False                            
        
        
def test_IC_7428():        
    testIC = IC_7428()
    m = {3:0 ,2:0 ,6:1 ,5:0 ,7:0 ,9:1 ,8:1 ,12:1 ,11:0 ,14:1}        
    testIC.setIC(m)
    n = {1:1 ,4:0 ,10:0, 13:0}
    if n != testIC.run():
        assert False                            
        
        
def test_IC_7430():        
    testIC = IC_7430()
    m = {1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,6:0 ,7:0 ,12:0 ,11:0 ,14:1}        
    testIC.setIC(m)
    n = { 8:1 }
    if n != testIC.run():
        assert False            

def test_IC_7432():        
    testIC = IC_7432()
    m = {1:1 ,2:1 ,4:0 ,5:0 ,7:0 ,9:0 ,10:0 ,12:0 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = { 3:1 ,6:0 ,8:0 ,11:1 }
    if n != testIC.run():
        assert False                                                
        
        
def test_IC_7433():        
    testIC = IC_7433()
    m = {3:1 ,2:1 ,6:0 ,5:0 ,7:0 ,9:0 ,8:0 ,12:0 ,11:1 ,14:1}        
    testIC.setIC(m)
    n = { 1:0 ,4:1 ,10:1 ,13:0 }
    if n != testIC.run():
        assert False                                                
        
        
        
def test_IC_7437():        
    testIC = IC_7437()
    m = {1:1 ,2:1 ,4:0 ,5:0 ,7:0 ,9:0 ,10:0 ,12:0 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = { 3:0 ,6:1 ,8:1 ,11:1 }
    if n != testIC.run():
        assert False
        

def test_IC_7438():        
    testIC = IC_7438()
    m = {1:1 ,2:1 ,4:0 ,5:0 ,7:0 ,9:0 ,10:0 ,12:0 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = { 3:0 ,6:1 ,8:1 ,11:1 }
    if n != testIC.run():
        assert False        
        
def test_IC_7440():        
    testIC = IC_7440()
    m = {1:1 ,2:1 ,4:0 ,5:0 ,7:0 ,9:0 ,10:0 ,12:0 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = { 6:1 ,8:1 }
    if n != testIC.run():
        assert False                
        
        
def test_IC_7451():        
    testIC = IC_7451()
    m = {3:1 ,2:1 ,4:1 ,5:1 ,7:0 ,1:0 ,13:0 ,12:0 ,11:1 ,9:1 ,10:1 ,14:1}        
    testIC.setIC(m)
    n = { 6:0 ,8:0 }
    if n != testIC.run():
        assert False                
        
def test_IC_7454():        
    testIC = IC_7454()
    m = {1:1 ,2:1 ,3:1 ,4:1 ,5:1 ,7:0 ,9:0 ,10:0 ,11:0 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = { 6:0 }
    if n != testIC.run():
        assert False                        
        
 
def test_IC_7455():        
    testIC = IC_7455()
    m = {1:1 ,2:1 ,3:1 ,4:1 ,7:0 ,10:0 ,11:0 ,12:1 ,13:1 ,14:1}        
    testIC.setIC(m)
    n = { 8:0 }
    if n != testIC.run():
        assert False                               
       
       

def test_IC_7458():        
    testIC = IC_7458()
    m = {2:1 ,3:1 ,4:1 ,5:1 ,7:0 ,9:1 ,10:1 ,11:1 ,1:0 ,13:0 ,12:1 ,14:1}        
    testIC.setIC(m)
    n = { 6:1 ,8:1 }
    if n != testIC.run():
        assert False                                
          
          
          
def test_IC_7464():        
    testIC = IC_7464()
    m = {2:1 ,3:1 ,1:1 ,4:0 ,5:0 ,6:0 ,7:0 ,9:1 ,10:1 ,11:1 ,12:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = { 8:0 }
    if n != testIC.run():
        assert False           
        
        
        
        
def test_IC_7486():        
    testIC = IC_7486()
    m = {1:1 ,2:1 ,4:0 ,5:0 ,7:0 ,9:0 ,10:1 ,12:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = { 3:0 ,6:0 ,8:1 ,11:1 }
    if n != testIC.run():
        assert False           
        
        

        
def test_IC_74260():        
    testIC = IC_74260()
    m = {1:1 ,2:1 ,3:0 ,4:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:1 ,13:0 ,14:1}        
    testIC.setIC(m)
    n = { 5:0 ,6:1 }
    if n != testIC.run():
        assert False   
        
def test_IC_741G00():        
    testIC = IC_741G00()
    m = {1:1 ,2:1 ,3:0 ,5:1 }        
    testIC.setIC(m)
    n = { 4:0 }
    if n != testIC.run():
        assert False       
        
        
def test_IC_741G02():        
    testIC = IC_741G02()
    m = {1:1 ,2:0 ,3:0 ,5:1 }        
    testIC.setIC(m)
    n = { 4:0 }
    if n != testIC.run():
        assert False       
        
def test_IC_741G03():        
    testIC = IC_741G03()
    m = {1:1 ,2:1 ,3:0 ,5:1 }        
    testIC.setIC(m)
    n = { 4:0 }
    if n != testIC.run():
        assert False       
        
def test_IC_741G04():        
    testIC = IC_741G04()
    m = { 2:1 ,3:0 ,5:1 }        
    testIC.setIC(m)
    n = { 4:0 }
    if n != testIC.run():
        assert False       
        
        
        
def test_IC_741G05():        
    testIC = IC_741G05()
    m = { 2:1 ,3:0 ,5:1 }        
    testIC.setIC(m)
    n = { 4:0 }
    if n != testIC.run():
        assert False       
        
        
def test_IC_741G08():        
    testIC = IC_741G08()
    m = { 1:1 ,2:1 ,3:0 ,5:1 }        
    testIC.setIC(m)
    n = { 4:1 }
    if n != testIC.run():
        assert False       
        
        
def test_IC_7431():        
    testIC = IC_7431()
    m = { 1:1 ,3:1 ,5:1 ,6:0 ,8:0 ,10:0 ,11:1 ,13:0 ,15:1 ,16:1 }        
    testIC.setIC(m)
    n = { 2:0 ,4:1 ,7:1 ,9:1 ,12:0 ,14:0 }
    if n != testIC.run():
        assert False       
        
def test_7442():
    
    testIC = IC_7442()
    
    p = [
    {12:0, 13:0, 14:0 ,15:0 ,8:0 ,16:1}, 
    {12:0, 13:0, 14:0 ,15:1 ,8:0 ,16:1},
    {12:0, 13:0, 14:1 ,15:0 ,8:0 ,16:1},
    {12:0, 13:0, 14:1 ,15:1 ,8:0 ,16:1},
    {12:0, 13:1, 14:0 ,15:0 ,8:0 ,16:1},
    {12:0, 13:1, 14:0 ,15:1 ,8:0 ,16:1},
    {12:0, 13:1, 14:1 ,15:0 ,8:0 ,16:1},
    {12:0, 13:1, 14:1 ,15:1 ,8:0 ,16:1},
    {12:1, 13:0, 14:0 ,15:0 ,8:0 ,16:1},
    {12:1, 13:0, 14:0 ,15:1 ,8:0 ,16:1} ]
    
    w =[
    {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 0, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 0, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 0} ]
    
    for i in range(len(p)):
        
        testIC.setIC(p[i])
        if w[i] != testIC.run():
            assert False    

    
            
            
def test_7443():
    
    testIC = IC_7443()
    
    p = [
    {12:0, 13:0, 14:1 ,15:1 ,8:0 ,16:1},
    {12:0, 13:1, 14:0 ,15:0 ,8:0 ,16:1},
    {12:0, 13:1, 14:0 ,15:1 ,8:0 ,16:1},
    {12:0, 13:1, 14:1 ,15:0 ,8:0 ,16:1},
    {12:0, 13:1, 14:1 ,15:1 ,8:0 ,16:1},
    {12:1, 13:0, 14:0 ,15:0 ,8:0 ,16:1},
    {12:1, 13:0, 14:0 ,15:1 ,8:0 ,16:1},
    {12:1, 13:0, 14:1 ,15:0 ,8:0 ,16:1},
    {12:1, 13:0, 14:1 ,15:1 ,8:0 ,16:1},
    {12:1, 13:1, 14:0 ,15:0 ,8:0 ,16:1} ]
    
    w =[
    {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 0, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 0, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 0} ]
    
    for i in range(len(p)):
        
        testIC.setIC(p[i])
        if w[i] != testIC.run():
            assert False
            
            
def test_7444():
    
    testIC = IC_7444()
    
    p = [
    {12:0, 13:0, 14:1 ,15:0 ,8:0 ,16:1},
    {12:0, 13:1, 14:0 ,15:0 ,8:0 ,16:1},
    {12:0, 13:1, 14:0 ,15:1 ,8:0 ,16:1},
    {12:0, 13:1, 14:1 ,15:0 ,8:0 ,16:1},
    {12:0, 13:1, 14:1 ,15:1 ,8:0 ,16:1},
    {12:1, 13:0, 14:1 ,15:0 ,8:0 ,16:1},
    {12:1, 13:1, 14:0 ,15:0 ,8:0 ,16:1},
    {12:1, 13:1, 14:0 ,15:1 ,8:0 ,16:1},
    {12:1, 13:1, 14:1 ,15:0 ,8:0 ,16:1},
    {12:1, 13:1, 14:1 ,15:1 ,8:0 ,16:1} ]
    
    w =[
    {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 0},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 0, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 0, 10: 1, 11: 1} ]
    
    for i in range(len(p)):
        
        testIC.setIC(p[i])
        
        if w[i] != testIC.run():
            assert False   
            
def test_7445():            
    testIC = IC_7445()
        
    p = [
        {12:0, 13:0, 14:0 ,15:0 ,8:0 ,16:1}, 
        {12:0, 13:0, 14:0 ,15:1 ,8:0 ,16:1},
        {12:0, 13:0, 14:1 ,15:0 ,8:0 ,16:1},
        {12:0, 13:0, 14:1 ,15:1 ,8:0 ,16:1},
        {12:0, 13:1, 14:0 ,15:0 ,8:0 ,16:1},
        {12:0, 13:1, 14:0 ,15:1 ,8:0 ,16:1},
        {12:0, 13:1, 14:1 ,15:0 ,8:0 ,16:1},
        {12:0, 13:1, 14:1 ,15:1 ,8:0 ,16:1},
        {12:1, 13:0, 14:0 ,15:0 ,8:0 ,16:1},
        {12:1, 13:0, 14:0 ,15:1 ,8:0 ,16:1} ]

    w =[
    {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0, 7: 1, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 9: 1, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 0, 10: 1, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 0, 11: 1},
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 0} ]

    for i in range(len(p)):
        
        testIC.setIC(p[i])
        
        if w[i] != testIC.run():
            assert False        
            
def test_74133():
    
    testIC = IC_74133()
    m = {1:1 ,2:1 ,3:1 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 ,10:1 ,11:1 ,12:1 ,13:0 ,14:1 ,15:0 ,16:1 }
    testIC.setIC(m)
        
    n = {9:1 }
    if n != testIC.run():
        assert False       
        
        
        
def test_7483():
    
    testIC = IC_7483()
    m = {1:1 ,3:1 ,4:0 ,5:1 ,7:0 ,8:0 ,10:1 ,11:1 ,12:0 ,13:0 ,16:1 }
    
    testIC.setIC(m)
        
    n = {9: 0, 2: 1, 14: 1, 6: 1, 15: 0}
    if n != testIC.run():
        assert False
