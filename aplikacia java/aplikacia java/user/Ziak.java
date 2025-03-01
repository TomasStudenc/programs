package user;


public class Ziak {
    private String id;
    private String prv_p;
    private String prv_t;
    private String druh_p;
    private String druh_t;
    
    public void set_id(String id){
        this.id=id;
    }
    public void set_prv_p(String volba){
        this.prv_p=volba;
    }
    public void set_prv_t(String volba){
        this.prv_t=volba;
    }
    public void set_druh_p(String volba){
        this.druh_p=volba;
    }
    public void set_druh_t(String volba){
        this.druh_t=volba;
    }
    public String get_id(){
        return this.id;
    }
    public String get_pp(){
        return this.prv_p;
    }
    public String get_dp(){
        return this.druh_p;
    }
    public String get_pt(){
        return this.prv_t;
    }
    public String get_dt(){
        return this.druh_t;
    }
}
