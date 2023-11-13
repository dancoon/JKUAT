public class Main {
    public static void main(String[] args) {

    }
}

class Shape {
    public void draw(){
        System.out.println("Drawing a shape");
    }
    public double calculateArea(){}
}

class Circle extends Shape{
    private double radius;

    Cylinder(double radius) {
        this.radius;
    }

    public void draw(){
        System.out.println("Drawing a shape");
    }

    public double calculateArea(){
        return 3.142 * this.radius * this.radius;
    }
}

class Cylinder extends Shape {
    private double radius;
    private double height;

    Cylinder(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    public void draw(){
        System.out.println("Drawing a shape");
    }    
    
    public double calculateArea(){
        return (2 * 3.142 * this.radius * this.radius) + (3.142 * 2 * this.radius * this.height);
    }
}
