public class Area {
    public static void main(String[] args) {
        
    }
}

class Polygon {
    int numberOfSides;
}

class Rectangle extends Polygon {
    double length;
    double width;

    double area(double side) {
        return side * side ;
    };
    Rectangle(double length, double width){
        this.length = length;
        this.width = width;
        super.numberOfSides = 4;
    }

    double area() {
        return this.length * this.width;
    }
}

class Square extends Polygon {
    double side;

    Square(double side) {
        this.side = side;
        super.numberOfSides = 4;
    }

    double area(){
        return this.side * this.side;
    }
}
