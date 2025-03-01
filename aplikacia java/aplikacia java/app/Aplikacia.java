package app;

public class Aplikacia {
    
    public static String error(int i){
        if (i==1){
            return "wrong id\n";  
        }else if(i==2){
            return  "Cannot apply to the same school twice\n";
        }else if(i==3){
            return "invalid input\n";
        }else if(i==4){
            return "invalid id\n";
        }else if(i==5){
            return "you must chose one\n";
        }else if(i==6){
            return "error forming chart";
        }else{
            return "All good\n";
        }
    }
    public static String lenChange(int x, boolean eng){
        if(x==0){
            if(eng){
                return "My school";
            }else{
                return "Moja škola";
            }
        }else if(x==1){
            if(eng){
                return "Statistic";
            }else{
                return "Štatistika";
            }
        }else if(x==2){
            if(eng){
                return "School with entrance exam code:";
            }else{
                return "Škola s prijímacou skúškou kod:";
            }
        }else if(x==3){
            if(eng){
                return "School with talent test code:";
            }else{
                return "Škola s talentovou skúškou kod:";
            }
        }else if(x==4){
            if(eng){
                return "Submit";
            }else{
                return "Prihlásiť";
            }
        }else if(x==5){
            if(eng){
                return "                                           if you don't want to choose write 0                              ";
            }else{
                return "                                            Ak si nechcete zvolit napíšte 0                                  ";
            }
        }else if(x==6){
            if(eng){
                return "exam school";
            }else{
                return "Školy s p. skúškou";
            }
        }else if(x==7){
            if(eng){
                return "talent school";
            }else{
                return "Školy s t. skúškou";
            }
        }else if(x==8){
            if(eng){
                return "new login";
            }else{
                return "nové prihlasenie";
            }
        }else if(x==9){
            if(eng){
                return "First term";
            }else{
                return "Prvý termín";
            }
        }else if(x==10){
            if(eng){
                return "Second term";
            }else{
                return "Druhý termín";
            }
        }else if(x==11){
            if(eng){
                return "Application count";
            }else{
                return "Počet príhlasok";
            }
        }else if(x==12){
            if(eng){
                return "School ID: ";
            }else{
                return "ID školy: ";
            }
        }else if(x==13){
            if(eng){
                return "School";
            }else{
                return "Škola";
            }
        }else if(x==14){
            if(eng){
                return "Application statistic";
            }else{
                return "Štatistika prihlášok";
            }
        }else if(x==15){
            if(eng){
                return "Submission successful";
            }else{
                return "Prihlásenie bolo úspešné";
            }
        }else if(x==16){
            if(eng){
                return "City";
            }else{
                return "Mesto";
            }
        }else if(x==17){
            if(eng){
                return "Field of study";
            }else{
                return "Štúdijne odbory";
            }
        }else if(x==18){
            if(eng){
                return "Students";
            }else{
                return "Žiaci";
            }
        }else if(x==19){
            if(eng){
                return "Type of exam";
            }else{
                return "Typ skúšky";
            }
        }else{
            return "";
        }
    }
}
