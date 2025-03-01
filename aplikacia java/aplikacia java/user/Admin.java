package user;

import filework.*;

public class Admin {
    
    public static int get_skolaP(int id,int index){
        String inter;
        inter=ReadfromFile.readfromfile("p", id);
        String[] parts = inter.split("\\s+"); 
        
        int[] value={0,0,0,0};
        for (int i = 1; i < parts.length; i++) {
             value[i] = Integer.parseInt(parts[i]); 
            
        }
        return value[index];
    }
    public static int get_skolaT(int id,int index){
        String inter;
        inter=ReadfromFile.readfromfile("t", id);
        String[] parts = inter.split("\\s+"); 
        
        int[] value={0,0,0,0};
        for (int i = 1; i < parts.length; i++) {
             value[i] = Integer.parseInt(parts[i]); 
            
        }
        return value[index];
    }
}
