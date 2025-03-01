package app;

import filework.WriteToFile;
import shool.Skola_p;
import shool.Skola_t;
import user.Ziak;
public class Prihlasenie {
    
    public static void prihlasenie(Ziak ziak){
        Skola_p[] s_p = new Skola_p[101];
        Skola_t[] s_t = new Skola_t[101];
        int[] honota_p={0,0,0,0};
        int[] honota_t={0,0,0,0};
        for(int i=0;i<101;i++){
            for(int k=1;k<4;k++){
                honota_p[k]=Skola_p.get_clen(i, k);
            }
            s_p[i]=new Skola_p();
            s_p[i].setCount(honota_p[1]);
            s_p[i].setPrv(honota_p[2]);
            s_p[i].setDruh(honota_p[3]);
            for(int k=1;k<4;k++){
                honota_t[k]=Skola_t.get_clen(i, k);
            }
            s_t[i]= new Skola_t();
            s_t[i].setCount(honota_t[1]);
            s_t[i].setPrv(honota_t[2]);
            s_t[i].setDruh(honota_t[3]);
            
        }
        if(ziak.get_pp().equals("0")){
            int clen_p_p=s_p[0].getPrv();
            int count_p_p= s_p[0].getCount();
            clen_p_p++;
            count_p_p++;
            s_p[0].setPrv(clen_p_p);
            s_p[0].setCount(count_p_p);
        }
        else{
        String volba_p_p=""+ziak.get_pp().charAt(1)+ziak.get_pp().charAt(2)+ziak.get_pp().charAt(3);
        int vysledok_volba_p_p=Integer.parseInt(volba_p_p);
        int clen_p_p=s_p[vysledok_volba_p_p].getPrv();
        int count_p_p= s_p[vysledok_volba_p_p].getCount();
        clen_p_p++;
        count_p_p++;
        s_p[vysledok_volba_p_p].setPrv(clen_p_p);
        s_p[vysledok_volba_p_p].setCount(count_p_p);
        }

        if(ziak.get_dp().equals("0")){
            int clen_d_p=s_p[0].getDruh();
            int count_d_p= s_p[0].getCount();
            clen_d_p++;
            count_d_p++;
            s_p[0].setDruh(clen_d_p);
            s_p[0].setCount(count_d_p);
        }
        else{
        String volba_d_p=""+ziak.get_dp().charAt(1)+ziak.get_dp().charAt(2)+ziak.get_dp().charAt(3);
        int vysledok_volba_d_p=Integer.parseInt(volba_d_p);
        int clen_d_p=s_p[vysledok_volba_d_p].getDruh();
        int count_d_p= s_p[vysledok_volba_d_p].getCount();
        clen_d_p++;
        count_d_p++;
        s_p[vysledok_volba_d_p].setDruh(clen_d_p);
        s_p[vysledok_volba_d_p].setCount(count_d_p);
        }
        if(ziak.get_pt().equals("0")){
            int clen_p_t=s_t[0].getPrv();
            int count_p_t= s_t[0].getCount();
            clen_p_t++;
            count_p_t++;
            s_t[0].setPrv(clen_p_t);
            s_t[0].setCount(count_p_t);
        }
        else{
        String volba_p_t=""+ziak.get_pt().charAt(1)+ziak.get_pt().charAt(2)+ziak.get_pt().charAt(3);
        int vysledok_volba_p_t=Integer.parseInt(volba_p_t);
        int clen_p_t=s_t[vysledok_volba_p_t].getPrv();
        int count_p_t= s_t[vysledok_volba_p_t].getCount();
        clen_p_t++;
        count_p_t++;
        s_t[vysledok_volba_p_t].setPrv(clen_p_t);
        s_t[vysledok_volba_p_t].setCount(count_p_t);
        }
        if(ziak.get_dt().equals("0")){
            int clen_d_t=s_t[0].getDruh();
            int count_d_t= s_t[0].getCount();
            clen_d_t++;
            count_d_t++;
            s_t[0].setDruh(clen_d_t);
            s_t[0].setCount(count_d_t);
        }
        else{
        String volba_d_t=""+ziak.get_dt().charAt(1)+ziak.get_dt().charAt(2)+ziak.get_dt().charAt(3);
        int vysledok_volba_d_t=Integer.parseInt(volba_d_t);
        int clen_d_t=s_t[vysledok_volba_d_t].getDruh();        
        int count_d_t= s_t[vysledok_volba_d_t].getCount();
        clen_d_t++;
        count_d_t++;
        s_t[vysledok_volba_d_t].setDruh(clen_d_t);
        s_t[vysledok_volba_d_t].setCount(count_d_t);
        }
        
        WriteToFile.fill_p_file(s_p);
        WriteToFile.fill_t_file(s_t);
    }
}
