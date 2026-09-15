import java.util.Scanner;

    public class pg{
        public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        
         double pddht = 8.45;
         double sddht = 9.00;
         double tddht = 7.45;
         double qddht = 8.30;
         double seddht = 6.00;
         double setddht = 7.40;

         double valor_por_hora = 8.90;

         double soma_de_horas_semanais = (pddht+sddht+tddht+qddht+seddht+setddht);

         double pagamento_da_semana = (soma_de_horas_semanais)*(valor_por_hora);


         System.out.println("Olá seu total de horas trabalhadas na semana foram " + soma_de_horas_semanais + " horas");
         System.out.println("E seu pagamente de horas é " + pagamento_da_semana + " Reais");



     }



    }







