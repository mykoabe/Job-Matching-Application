import { Component, OnInit } from '@angular/core';
import { AuthService } from '../AuthService/auth.service';
import { Works } from '../works';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  title = 'FinalJobMatching';
  
  constructor(private _auth : AuthService){}

  registerEmployeeData = {username: '', email: '', password: ''}
  registerEmployerData = {username: '', email: '', password: '', address: ''}
  ngOnInit(){}
  registerEmployee(){
    this._auth.registerEmployee(this.registerEmployeeData)
    .subscribe(
      res=>console.log(res),
      err=>console.log(err)
      )
  }
  registerEmployer(){
    this._auth.registerEmployer(this.registerEmployerData)
    .subscribe(
      res=>console.log(res),
      err=>console.log(err)
      )
  }

}
