import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../AuthService/auth.service';

@Component({
  selector: 'app-employee-login',
  templateUrl: './employee-login.component.html',
  styleUrls: ['./employee-login.component.css']
})
export class EmployeeLoginComponent implements OnInit {
  loginEmployeeData = {email: '', password: ''}
  constructor(private _auth: AuthService,
              private _router: Router ) { }
  ngOnInit(): void {
  }
  loginEmployee(){
    this._auth.loginEmployee(this.loginEmployeeData)
    .subscribe(
      res=> {
        console.log(res)
        localStorage.setItem('token', res.access_token)
        this._router.navigate(["/jobs"])
      },
      err=>console.log(err)
      )
  }
  
}
