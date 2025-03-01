package gui;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.PieChart;
import javafx.scene.chart.XYChart;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.util.*;
import app.*;
import filework.*;
import user.*;
//--------------------------------------------------------------------
public class AppGUI extends Application {
//======================================================
private ScrollPane scroll = new ScrollPane();	
private TextArea output = new TextArea();
private TextArea lastCheck=new TextArea();
private TextArea ziakout= new TextArea();	
//======================================================
private Label primSkola = new Label();
private Label taletSkola= new Label();
private Label osemmiest= new Label("<--------------| **** **** ID|            ");
private Label noChose= new Label();
private Label push=new Label("          ");
//======================================================
private TextField idAcces= new TextField();
private TextField prvP=new TextField();
private TextField druhP=new TextField();
private TextField prvT=new TextField();
private TextField druhT=new TextField();
//======================================================
private Button login = new Button("✓");
private Button prihlas=new Button();
private Button ziaci = new Button();
private Button mojaskola= new Button();
private Button statistika= new Button();
private Button reRegister= new Button();
//======================================================
private Image logo= new Image("file:logo_oop1.png");
private Image kamNa= new Image("file:kam_na1.png");
private Image kamNNa=new Image("file:kam_na.png");
private Image flag=new Image("file:flagg.png");
//--------------------------------------------------------------------
    Ziak ziak= new Ziak();
    public boolean eng=false;
	public void start(Stage mainWindow) {
        MenuBar menuBar = new MenuBar();
        Menu search = new Menu(Aplikacia.lenChange(16, eng));
        MenuItem ttItem = new MenuItem("Trnava");
        MenuItem baItem = new MenuItem("Bratislava");
        MenuItem ziItem = new MenuItem("Žilina");
        MenuItem prItem = new MenuItem("Prešov");
        MenuItem nrItem = new MenuItem("Nitra");
        MenuItem pnItem = new MenuItem("Piešťany");
        MenuItem krItem = new MenuItem("Košice");
        MenuItem bbItem = new MenuItem("Banská Bystrica");
        MenuItem miItem = new MenuItem("Michalovce");
        MenuItem huItem = new MenuItem("Humenné");
        MenuItem brItem = new MenuItem("Bardejov");
        MenuItem koItem = new MenuItem("Kolárovo");
        MenuItem gaItem = new MenuItem("Galanta");
        MenuItem peItem = new MenuItem("Pezinok");
        MenuItem mrItem = new MenuItem("Martin");
        MenuItem zvItem = new MenuItem("Zvolen");
        MenuItem scItem = new MenuItem("Senec");
        MenuItem trItem = new MenuItem("Trenčín");
        MenuItem lmItem = new MenuItem("Liptovský Mikuláš");
        MenuItem ljItem = new MenuItem("Liptovský Ján");
        search.getItems().addAll(ttItem,baItem,ziItem,prItem,nrItem,pnItem,krItem,bbItem,miItem,huItem,brItem,koItem,gaItem,peItem,mrItem,zvItem,scItem,trItem,lmItem,ljItem);
        //----------------------------------------------------------------------
        Menu typMenu= new Menu(Aplikacia.lenChange(17, eng));
        MenuItem bil= new MenuItem("Bilingválna");
        MenuItem obch= new MenuItem("Obchodná");
        MenuItem elek = new MenuItem("Elektrotechnická");
        MenuItem poln= new MenuItem("Polnohospodárska");
        MenuItem gym= new MenuItem("Gymnázium");
        MenuItem sport= new MenuItem("Športová");
        MenuItem mali= new MenuItem("Maliarska");
        MenuItem hud = new MenuItem("Hudobná");
        MenuItem soch= new MenuItem("Sochárska");
        MenuItem kuch= new MenuItem("Kuchárska");
        typMenu.getItems().addAll(bil,obch,elek,poln,gym,sport,mali,hud,soch,kuch);
        //-----------------------------------------------------------------------
        Menu druh = new Menu(Aplikacia.lenChange(19, eng));
        MenuItem list_p = new MenuItem(Aplikacia.lenChange(6, eng));
        MenuItem list_t = new MenuItem(Aplikacia.lenChange(7, eng));
        druh.getItems().addAll(list_p,list_t);
        //-----------------------------------------------------------------------
        menuBar.getMenus().addAll(search,typMenu,druh);
        ImageView startImage= new ImageView(logo);
        startImage.setFitWidth(550);
        startImage.setFitHeight(500);
        //--------------------------------------------------------------------
        ImageView kamImage= new ImageView(kamNa);
        kamImage.setFitWidth(550);
        kamImage.setFitHeight(50);
        //--------------------------------------------------------------------
        ImageView kam2Image= new ImageView(kamNNa);
        kam2Image.setFitWidth(550);
        kam2Image.setFitHeight(50);
        //--------------------------------------------------------------------
		mainWindow.setTitle("Kam na strednú");
        mainWindow.setMaxWidth(550);
        mainWindow.setMaxHeight(570);
        //--------------------------------------------------------------------
        ImageView flagImage= new ImageView(flag);
        flagImage.setFitHeight(20);
        flagImage.setFitWidth(30);
        //--------------------------------------------------------------------
        ToggleButton engBut = new ToggleButton("Off");
        lastCheck.setPrefHeight(120);
        lastCheck.setPrefWidth(550);
        ziakout.setPrefHeight(405);
        ziakout.setPrefWidth(550);
        output.setPrefWidth(550);
        engBut.setSelected(false);
        //--------------------------------------------------------------------
		FlowPane pane = new FlowPane();
        pane.setStyle("-fx-background-color: lightgrey;");
        //--------------------------------------------------------------------
        pane.getChildren().add(startImage);
        pane.getChildren().add(push);
        pane.getChildren().add(idAcces);
        pane.getChildren().add(login);
        pane.getChildren().add(osemmiest);
        pane.getChildren().add(flagImage);
		pane.getChildren().add(engBut);
        //--------------------------------------------------------------------
        scroll.setContent(pane);
    engBut.setOnAction(event -> {
            if (engBut.isSelected()) {
                engBut.setText("On");
                eng=true;
            } else {
                engBut.setText("Off");
                eng=false;
            }
        });
login.setOnAction(e -> {
    pane.getChildren().removeAll(startImage,login,idAcces,osemmiest,engBut,flagImage,push);
    mojaskola.setText(Aplikacia.lenChange(0, eng));
    statistika.setText(Aplikacia.lenChange(1, eng));
    primSkola.setText(Aplikacia.lenChange(2, eng));
    taletSkola.setText(Aplikacia.lenChange(3, eng)); 
    prihlas.setText(Aplikacia.lenChange(4, eng));
    noChose.setText(Aplikacia.lenChange(5, eng));
    list_p.setText(Aplikacia.lenChange(6, eng));
    list_t.setText(Aplikacia.lenChange(7, eng));
    reRegister.setText(Aplikacia.lenChange(8, eng));
    ziaci.setText(Aplikacia.lenChange(18, eng));
    //--------------------------------------------------------------------
    String loginID= idAcces.getText();
        if(loginID.length()!=8){
            pane.getChildren().addAll(kamImage,idAcces,login,osemmiest,output,kam2Image); 
            output.appendText(app.Aplikacia.error(1));
        }else if((loginID.charAt(0)=='S' || loginID.charAt(0)=='s')&& (loginID.charAt(1)=='K' || loginID.charAt(1)=='k') && (loginID.charAt(2)=='O' || loginID.charAt(2)=='o') && (loginID.charAt(3)=='L' || loginID.charAt(3)=='l' )){
            pane.getChildren().removeAll(output,kamImage,kam2Image);
            //--------------------------------------------------------------------
            pane.getChildren().add(startImage);
            pane.getChildren().add(mojaskola);
            pane.getChildren().add(statistika);
            
            pane.getChildren().add(ziaci);
        }else{
            pane.getChildren().remove(startImage);
            pane.getChildren().removeAll(login,idAcces,output,engBut,flagImage);
            output.clear();
         //--------------------------------------------------------------------   
            int idcheck=ReadfromFile.readid(Integer.parseInt(loginID));
            if(idcheck==0){
                pane.getChildren().clear();
                pane.getChildren().addAll(kamImage,idAcces,login,output,kam2Image);
                 idcheck=ReadfromFile.readid(Integer.parseInt(loginID));
                 String out = ReadfromFile.logsearch(loginID);
                 String [] slip = out.split("\\s+");
                 output.appendText("ID:"+slip[0]+"\n"+Aplikacia.lenChange(6, eng)+":\n"+Aplikacia.lenChange(9, eng)+": "+slip[1]+"\n"+Aplikacia.lenChange(10, eng)+": "+slip[2]+"\n"+Aplikacia.lenChange(7, eng)+":\n"+Aplikacia.lenChange(9, eng)+": "+slip[3]+"\n"+Aplikacia.lenChange(10, eng)+": "+slip[4]);
            }else{
            pane.getChildren().removeAll(kamImage,kam2Image);
            
            pane.getChildren().addAll(kamImage,menuBar,output);
           
            
            //--------------------------------------------------------------------
            output.setText("ID:"+ loginID +"\n");
            //--------------------------------------------------------------------
            //pane.getChildren().add(list_p);
            //pane.getChildren().add(list_t);
            //--------------------------------------------------------------------
            pane.getChildren().remove(login);
            pane.getChildren().remove(idAcces);
            pane.getChildren().remove(osemmiest);
            //--------------------------------------------------------------------
            pane.getChildren().addAll(push,noChose ,primSkola, prvP, druhP, taletSkola, prvT, druhT, prihlas,kam2Image);     
        }
        }
    
    });
    reRegister.setOnAction(e->{
        pane.getChildren().clear();
        pane.getChildren().addAll(startImage,push,idAcces,login,osemmiest,flagImage,engBut);   

        //--------------------------------------------------------------------
        prvP.clear();
        prvT.clear();
        druhP.clear();
        druhT.clear();
        lastCheck.clear();
    });
    //menu bar search ============================================================
    ttItem.setOnAction(e -> {
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Trnava")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Trnava")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    baItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Bratislava")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Bratislava")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    ziItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Žilina")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Žilina")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    prItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Prešov")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Prešov")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    nrItem.setOnAction(e->{ 
       output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Nitra")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Nitra")) { 
                output.appendText(cache + "\n");
            }
        }});
    pnItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Piešťany")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Piešťany")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    krItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Košice")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Košice")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    bbItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Banska Bistrica")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Banska Bistrica")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    miItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Michalovce")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Michalovce")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    huItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Humenné")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Humenné")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    brItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Bardejov")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Bardejov")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    koItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Kolárovo")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Kolárovo")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    gaItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Galanta")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Galanta")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    peItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Pezinok")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Pezinok")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    mrItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Martin")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Martin")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    zvItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Zvolen")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Zvolen")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    scItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Senec")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Senec")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    trItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Trenčín")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Trenčín")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    lmItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Liptovský Mikulaš")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Liptovský Mikulaš")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    ljItem.setOnAction(e->{
        output.clear();
        String cache = "";
        output.appendText(Aplikacia.lenChange(7, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("Liptovský Ján")) { 
                output.appendText(cache + "\n");
            }
        }
        output.appendText(Aplikacia.lenChange(6, eng)+":\n");
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Liptovský Ján")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    bil.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("bilingválna")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    obch.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("obchodná")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    elek.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("elektrotechnická")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    poln.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("polnohospodarska")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    gym.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("p", i);
            if (cache.contains("Gymnazium")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    sport.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("športová")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    mali.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("maliarska")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    hud.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("hudobná")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    soch.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("sochárska")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    kuch.setOnAction(e->{
        output.clear();
        String cache = "";
        for (int i = 0; i < 100; i++) {
            cache = ReadfromFile.list_all("t", i);
            if (cache.contains("kuchárska")) { 
                output.appendText(cache + "\n");
            }
        }
    });
    //menu bar search end ===========================================
    mojaskola.setOnAction(e->{
        
        String loginID= idAcces.getText();
        int[] value={0,0,0,0};
        if(loginID.charAt(4)=='t'||loginID.charAt(4)=='T'){
            String ktora= ""+loginID.charAt(5)+loginID.charAt(6)+loginID.charAt(7);
            for(int i=1;i<4;i++){
                value[i]= Admin.get_skolaT(Integer.parseInt(ktora),i);
        }
        pane.getChildren().removeAll(startImage,idAcces,login,output,osemmiest);
        //--------------------------------------------------------------------
        ObservableList<PieChart.Data> pieChartData =
             FXCollections.observableArrayList(
             new PieChart.Data(Aplikacia.lenChange(9, eng)+"\n"+value[2],value[2]),
             new PieChart.Data(Aplikacia.lenChange(10, eng)+"\n"+value[3], value[3]),
             new PieChart.Data(Aplikacia.lenChange(11, eng)+"\n"+value[1],0));
    String ID_skola_out=""+loginID.charAt(4)+loginID.charAt(5)+loginID.charAt(6)+loginID.charAt(7); 
     final PieChart chart = new PieChart(pieChartData);
     chart.setTitle(Aplikacia.lenChange(12, eng)+ID_skola_out);
    //--------------------------------------------------------------------
     pane.getChildren().clear();
     
     pane.getChildren().addAll(kamImage,mojaskola,statistika,ziaci,chart);
        }else if(loginID.charAt(4)=='p'||loginID.charAt(4)=='P'){
            String ktora= ""+loginID.charAt(5)+loginID.charAt(6)+loginID.charAt(7);
            for(int i=1;i<4;i++){
            value[i]= Admin.get_skolaP(Integer.parseInt(ktora),i);
        }
        pane.getChildren().removeAll(startImage,idAcces,login,output,osemmiest);
        //--------------------------------------------------------------------
        ObservableList<PieChart.Data> pieChartData =
             FXCollections.observableArrayList(
                new PieChart.Data(Aplikacia.lenChange(9, eng)+"\n"+value[2],value[2]),
                new PieChart.Data(Aplikacia.lenChange(10, eng)+"\n"+value[3], value[3]),
                new PieChart.Data(Aplikacia.lenChange(11, eng)+"\n"+value[1],0));
    //--------------------------------------------------------------------
    String ID_skola_out=""+loginID.charAt(4)+loginID.charAt(5)+loginID.charAt(6)+loginID.charAt(7); 
        final PieChart chart = new PieChart(pieChartData);
        chart.setTitle(Aplikacia.lenChange(12, eng)+ID_skola_out);
        pane.getChildren().clear();
        pane.getChildren().addAll(kamImage,mojaskola,statistika,ziaci,chart);
        }else{
            pane.getChildren().add(output);
            output.appendText(Aplikacia.error(6));
        }
            pane.getChildren().addAll(reRegister,kam2Image);    
    });
    statistika.setOnAction(e -> {
        
        String loginID= idAcces.getText();
        pane.getChildren().clear();
        pane.getChildren().add(kamImage);
        //--------------------------------------------------------------------
        if(loginID.charAt(4)=='t'||loginID.charAt(4)=='T'){
        final CategoryAxis xAxis = new CategoryAxis();
        final NumberAxis yAxis = new NumberAxis();
        //--------------------------------------------------------------------
        xAxis.setLabel(Aplikacia.lenChange(13, eng));
        //--------------------------------------------------------------------
        final LineChart<String, Number> lineChart = new LineChart<>(xAxis, yAxis);
        //--------------------------------------------------------------------
        lineChart.setTitle(Aplikacia.lenChange(14, eng));
        //--------------------------------------------------------------------
        XYChart.Series<String, Number> series = new XYChart.Series<>();
        //--------------------------------------------------------------------
        series.setName(Aplikacia.lenChange(11, eng));
        //--------------------------------------------------------------------
        for (int i=1;i<100;i++){
        int value= Admin.get_skolaT(i,1);
        if(value==0){
            continue;
        }
        series.getData().add(new XYChart.Data<>(""+i,value));
        }
        lineChart.getData().add(series);
        pane.getChildren().addAll(mojaskola, statistika,ziaci, lineChart);
        }else if(loginID.charAt(4)=='p'||loginID.charAt(4)=='P'){
            final CategoryAxis xAxis = new CategoryAxis();
            final NumberAxis yAxis = new NumberAxis();
            //--------------------------------------------------------------------
            xAxis.setLabel(Aplikacia.lenChange(13, eng));
            //--------------------------------------------------------------------
            final LineChart<String, Number> lineChart = new LineChart<>(xAxis, yAxis);
            //--------------------------------------------------------------------
            lineChart.setTitle(Aplikacia.lenChange(14, eng));
            //--------------------------------------------------------------------
            XYChart.Series<String, Number> series = new XYChart.Series<>();
            //--------------------------------------------------------------------
            series.setName(Aplikacia.lenChange(11, eng));
            //--------------------------------------------------------------------
            for (int i=1;i<100;i++){
            int value= Admin.get_skolaP(i,1);
            if(value==0){
                continue;
            }
            series.getData().add(new XYChart.Data<>(""+i,value));
            }
            lineChart.getData().add(series);
            pane.getChildren().addAll(mojaskola, statistika,ziaci, lineChart);
        }else{
            pane.getChildren().add(output);
            output.appendText(Aplikacia.error(6));
        }
        pane.getChildren().addAll(reRegister,kam2Image);
    });
    //-------------------------------------------------------------------------------------
    ziaci.setOnAction(e->{
        pane.getChildren().clear();
        ziakout.clear();
        pane.getChildren().addAll(kamImage,mojaskola,statistika,ziaci,ziakout,reRegister,kam2Image);
        String work= idAcces.getText();
        
            String premen= ""+work.toLowerCase().charAt(4)+work.charAt(5)+work.charAt(6)+work.charAt(7);
            List<String> searched= ReadfromFile.ziaklog(premen);
            for (String line : searched){
                String[] slip= line.split("\\s+");
               
                if(work.charAt(4)=='t'||work.charAt(4)=='T'){
                    if(premen.equals(slip[3].toLowerCase())){
                        ziakout.appendText("ID: "+slip[0]+"     "+Aplikacia.lenChange(9, eng)+"\n");
                    }else if(premen.equals(slip[4].toLowerCase())){
                        ziakout.appendText("ID: "+slip[0]+"     "+Aplikacia.lenChange(10, eng)+"\n");
                    }

                }
                if(work.charAt(4)=='p'||work.charAt(4)=='P'){
                   if(premen.equals(slip[1].toLowerCase())){
                        ziakout.appendText("ID: "+slip[0]+"     "+Aplikacia.lenChange(9, eng)+"\n");
                    }else if(premen.equals(slip[2].toLowerCase())){
                        ziakout.appendText("ID: "+slip[0]+"     "+Aplikacia.lenChange(10, eng)+"\n");
                    }

                }
            }
        
        

    });
    prihlas.setOnAction(e->{
        String p_p, d_p, p_t, d_t,x ;
        //--------------------------------------------------------------------
        p_p =prvP.getText();
        d_p =druhP.getText();
        p_t =prvT.getText();
        d_t =druhT.getText();
        //--------------------------------------------------------------------
        prvP.clear();
        prvT.clear();
        druhP.clear();
        druhT.clear();
        x=idAcces.getText();
        //--------------------------------------------------------------------
         if(p_p.isEmpty()||d_p.isEmpty()||p_t.isEmpty()||d_t.isEmpty()){
            output.appendText(Aplikacia.error(3));
        }else if((p_p.charAt(0)!='p'&&p_p.charAt(0)!='P'&&p_p.charAt(0)!='0')||(d_p.charAt(0)!='p'&&d_p.charAt(0)!='P'&&d_p.charAt(0)!='0')||(p_t.charAt(0)!='t'&&p_t.charAt(0)!='T'&&p_t.charAt(0)!='0')||(d_t.charAt(0)!='t'&&d_t.charAt(0)!='T'&&d_t.charAt(0)!='0')){
            output.appendText(Aplikacia.error(3));
        }else if((p_p.equals("P000")||p_p.equals("p000")||p_p.equals("0"))&&(d_p.equals("P000")||d_p.equals("p000")||d_p.equals("0"))&&(p_t.equals("T000")||p_t.equals("t000")||p_t.equals("0"))&&(d_t.equals("T000")||d_t.equals("t000")||d_t.equals("0"))){
            output.appendText(Aplikacia.error(5));
        }else if((p_p.toLowerCase().equals(d_p.toLowerCase())||p_t.toLowerCase().equals(d_t.toLowerCase()))&&(p_p.charAt(0)!='0'&&d_p.charAt(0)!='0'&&p_t.charAt(0)!='0'&&d_t.charAt(0)!='0')){
            output.appendText(Aplikacia.error(2));
        }else{
        pane.getChildren().removeAll(prihlas,kam2Image);
        pane.getChildren().addAll(reRegister,lastCheck,kam2Image);
        //--------------------------------------------------------------------
        ziak.set_id(x);
        ziak.set_prv_p(p_p);
        ziak.set_druh_p(d_p);
        ziak.set_prv_t(p_t);
        ziak.set_druh_t(d_t);
        //--------------------------------------------------------------------
        WriteToFile.writer_data(ziak);
        lastCheck.appendText(Aplikacia.lenChange(6, eng)+":\n"+Aplikacia.lenChange(9, eng)+": "+ziak.get_pp()+"\n"+Aplikacia.lenChange(10, eng)+": "+ziak.get_dp()+"\n"+Aplikacia.lenChange(7, eng)+":\n"+Aplikacia.lenChange(9, eng)+": "+ziak.get_pt()+"\n"+Aplikacia.lenChange(10, eng)+": "+ziak.get_dt());
        Prihlasenie.prihlasenie(ziak);
        output.appendText(Aplikacia.lenChange(15, eng));
        }
    });
    list_p.setOnAction(e->{
        output.clear();
        output.appendText(Aplikacia.lenChange(6, eng)+"\n");
        for(int i=0;i<100;i++){
            output.appendText(ReadfromFile.list_all("p", i)+"\n");
        }
    });
    list_t.setOnAction(e->{
        output.clear();
        output.appendText(Aplikacia.lenChange(7, eng)+"\n");
        for(int i=0;i<100;i++){
            output.appendText(ReadfromFile.list_all("t", i)+"\n");
        }
    });  

    mainWindow.setScene(new Scene(scroll, 550, 570)); // with scrollbars
	mainWindow.show();
    
}
public static void main(String[] args) {
    launch(args);
}
}