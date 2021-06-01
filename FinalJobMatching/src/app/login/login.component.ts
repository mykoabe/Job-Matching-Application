import { Component, OnInit } from '@angular/core';
import { AuthService } from '../AuthService/auth.service';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginUserData = {username: '', email: '', password: ''}
  constructor(private _auth: AuthService) {}
  ngOnInit(): void {
  }
  loginUser(){
    this._auth.registerEmployee(this.loginUserData)
    .subscribe(
      res=>console.log(res),
      err=>console.log(err)
      )
  }
}
