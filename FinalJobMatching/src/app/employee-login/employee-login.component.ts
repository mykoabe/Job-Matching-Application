import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../AuthService/auth.service';
import { JobService } from '../JobService/job.service';

@Component({
  selector: 'app-employee-login',
  templateUrl: './employee-login.component.html',
  styleUrls: ['./employee-login.component.css']
})
export class EmployeeLoginComponent implements OnInit {
  loginEmployeeData = {email: '', password: ''}
  loginEmployerData = {email: '', password: ''}
  jobs = []
  constructor(private _auth: AuthService,
              private _router: Router,
              private _jobservice: JobService ) { }
  ngOnInit(): void {
    this._auth.getEmployers()
    .subscribe
      (
        res=>this.jobs = res, 
        err=>console.log(err)
      )
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
  loginEmployer(){
    this._auth.loginEmployer(this.loginEmployerData)
    .subscribe(
      res=> {
        console.log(res)
        localStorage.setItem('token', res.access_token)
        // this._router.navigate(["/home"])
      },
      err=>console.log(err)
      )
  }
}
