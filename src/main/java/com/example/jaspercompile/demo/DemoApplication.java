package com.example.jaspercompile.demo;

import net.sf.jasperreports.engine.JRException;
import net.sf.jasperreports.engine.util.JRLoader;
import net.sf.jasperreports.engine.xml.JRXmlWriter;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperReport;

import java.io.File;

public class DemoApplication {

	public static void main(String[] args) {

		// compile = jrxml -> jasper
		// convert = jasper -> jrxml
		String operationMode = "compile";

		// Specify the directory paths
		String jrxmlDirectoryPath = "C:\\Users\\MLMNL-MFAJARDO\\Documents\\test\\testjava\\demo\\src\\main\\resources\\jrxml";
		String jasperDirectoryPath = "C:\\Users\\MLMNL-MFAJARDO\\Documents\\test\\testjava\\demo\\src\\main\\resources\\jasper";

		// Create the output directory if it doesn't exist
		File jasperDirectory = new File(jasperDirectoryPath);
		if (!jasperDirectory.exists()) {
			jasperDirectory.mkdirs();
		}

		if ("compile".equalsIgnoreCase(operationMode)) {
			compileJrxmlToJasper(jrxmlDirectoryPath, jasperDirectoryPath);
		} else if ("convert".equalsIgnoreCase(operationMode)) {
			convertJasperToJrxml(jasperDirectoryPath, jrxmlDirectoryPath);
		} else {
			throw new IllegalArgumentException("Invalid operation mode. Use 'compile' or 'convert'.");
		}
	}

	private static void compileJrxmlToJasper(String jrxmlDirectoryPath, String jasperDirectoryPath) {
		File jrxmlDirectory = new File(jrxmlDirectoryPath);
		File[] jrxmlFiles = jrxmlDirectory.listFiles((dir, name) -> name.toLowerCase().endsWith(".jrxml"));

		if (jrxmlFiles != null) {
			for (File jrxmlFile : jrxmlFiles) {
				try {
					String jasperFilePath = jasperDirectoryPath + "\\" + getFileNameWithoutExtension(jrxmlFile.getName()) + ".jasper";
					JasperCompileManager.compileReportToFile(jrxmlFile.getAbsolutePath(), jasperFilePath);
					System.out.println("Jasper report compiled successfully. Compiled file saved at: " + jasperFilePath);
				} catch (JRException e) {
					throw new RuntimeException("Error compiling Jasper report: " + jrxmlFile.getName(), e);
				}
			}
		} else {
			throw new RuntimeException("No .jrxml files found in directory: " + jrxmlDirectoryPath);
		}
	}

	private static void convertJasperToJrxml(String jasperDirectoryPath, String jrxmlDirectoryPath) {
		File jasperDirectory = new File(jasperDirectoryPath);
		File[] jasperFiles = jasperDirectory.listFiles((dir, name) -> name.toLowerCase().endsWith(".jasper"));

		if (jasperFiles != null) {
			for (File jasperFile : jasperFiles) {
				try {
					String jrxmlFilePath = jrxmlDirectoryPath + "\\" + getFileNameWithoutExtension(jasperFile.getName()) + ".jrxml";
					JasperReport report = (JasperReport) JRLoader.loadObject(jasperFile);
					JRXmlWriter.writeReport(report, jrxmlFilePath, "UTF-8");
					System.out.println("Jasper report converted successfully. Converted file saved at: " + jrxmlFilePath);
				} catch (JRException e) {
					throw new RuntimeException("Error converting Jasper report: " + jasperFile.getName(), e);
				}
			}
		} else {
			throw new RuntimeException("No .jasper files found in directory: " + jasperDirectoryPath);
		}
	}

	// Helper method to get file name without extension
	private static String getFileNameWithoutExtension(String fileName) {
		int dotIndex = fileName.lastIndexOf('.');
		return (dotIndex == -1) ? fileName : fileName.substring(0, dotIndex);
	}
}
