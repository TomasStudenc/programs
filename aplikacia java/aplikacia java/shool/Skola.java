package shool;

public class Skola implements Organizacia {
   public int count;
   public int prv;
   public int druh;
    public Skola(){

    }
    public Skola(int count){
        setCount(count);
    }
    public Skola(int count,int prv){
        setCount(count);
        setPrv(prv);
    }
    public Skola(int count,int prv,int druh){
        setCount(count);
        setPrv(prv);
        setDruh(druh);
    }
    
    public  void setCount(int count){
        this.count = count;
    }
    public void setPrv(int prv){
        this.prv=prv;
    }
    public void setDruh(int druh){
        this.druh=druh;
    }

    public int getCount(){
        return this.count;
    }
    public int getPrv(){
        return this.prv;
    }
    public int getDruh(){
        return this.druh;
    }   
}
