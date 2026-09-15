import java.util.Scanner;
    public class Main{
        public static void main(String[] args){
            Scanner entrada = new Scanner(System.in);
            
            System.out.print("Digite seu nome: ");
            String nome = entrada.nextLine();
            
            System.out.println(nome);
            
            System.out.print("Digite sua senha: ");
            String senha = entrada.nextLine();
            
            System.out.println(senha);
            
            String senha1 = (senha);
            String nome2= (nome);

if("admin".equals(nome2) && "1234".equals(senha1)){
    System.out.println("Permitido ");
    
    
}else{
    System.out.println("negado ");
    
    
    
