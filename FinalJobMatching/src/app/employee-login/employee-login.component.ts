import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-employee-login',
  templateUrl: './employee-login.component.html',
  styleUrls: ['./employee-login.component.css']
})
export class EmployeeLoginComponent implements OnInit {
  loginEmployeeData = {email: '', password: ''}

  constructor() { }

  ngOnInit(): void {
  }
  loginEmployee(){
    console.log(this.loginEmployeeData)
  }

}
