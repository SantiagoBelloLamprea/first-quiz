package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
  private int money;

  public static VendingMachine getInstance() {
    VendingMachine machine = new VendingMachineImpl();
    return machine;
  }

  public VendingMachineImpl() {
    this.money = 0;
  }

  @Override
  public void insertQuarter() {
    this.money += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

    // BEBIDA SCOTTCOLA
    if ("ScottCola".equals(name)) {
      if (money >= 75) {
        money -= 75;
        return new ScottCola();
      } else {
        throw new NotEnoughMoneyException();
      }
      // BEBIDA KARENTEA
    } else if ("KarenTea".equals(name)) {
      if (money >= 100) {
        money -= 100;
        return new KarenTea();
      } else {
        throw new NotEnoughMoneyException();
        // System.out.println("aqui");
      }
    } else {
      throw new UnknownDrinkException();
    }

  }
}

class ScottCola implements Drink {

  @Override
  public String getName() {
    return "ScottCola";
  }

  @Override
  public boolean isFizzy() {
    return true;
  }

}

class KarenTea implements Drink {

  @Override
  public String getName() {
    return "KarenTea";
  }

  @Override
  public boolean isFizzy() {
    return false;
  }
}
