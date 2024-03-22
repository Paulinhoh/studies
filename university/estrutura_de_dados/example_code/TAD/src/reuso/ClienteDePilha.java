package reuso;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class ClienteDePilha {
	
	public static void main(String[] args) throws IOException {

		//Pilha
		Stack<String> pilha = new Stack<String>();
		
		BufferedReader reader = new BufferedReader((new InputStreamReader
				(new FileInputStream(new File("São Paulo.txt")), "Cp1252")));

		String line = reader.readLine();

		while (line != null) {
			
			//Inserção do elemento
			pilha.push(line);	

			line = reader.readLine();
		}

		System.out.println("Pilha contém " + pilha.size() + " elementos");
		reader.close();
	}
}