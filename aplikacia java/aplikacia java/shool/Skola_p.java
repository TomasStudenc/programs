package shool;
import filework.*;
public class Skola_p extends Skola{

    public static int get_clen(int id, int index){
        String inter;
        inter=ReadfromFile.readfromfile("p", id);
        String[] parts = inter.split("\\s+"); 
        
        int[] value={0,0,0,0};
        for (int i = 1; i < parts.length; i++) {
             value[i] = Integer.parseInt(parts[i]); 
            
        }
        return value[index];
    };
    public void setCount(int count){
        super.setCount(count);
    }
    public void setPrv(int prv){
        super.setPrv(prv);
    }
    public void setDruh(int druh){
        super.setDruh(druh);
    }
    public int getCount(){
        return super.getCount();
    }
    public int getPrv(){
        return super.getPrv();
        }
    public int getDruh(){
        return super.getDruh();
    }

}
