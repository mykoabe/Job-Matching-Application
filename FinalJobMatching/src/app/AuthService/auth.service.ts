import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _registerUrlEmployee = "http://localhost:5000/api/employees"
  private _registerUrlEmployer = "http://localhost:5000/api/employers"
  private _loginUrlEmployee = "http://localhost:5000/api/loginEmployee"
  constructor(private http: HttpClient) { }

  registerEmployee(employee){
    return this.http.post<any>(this._registerUrlEmployee, employee)
  }
  registerEmployer(employer){
    return this.http.post<any>(this._registerUrlEmployer, employer)
  }
  loginEmployee(employee){
    return this.http.post<any>(this._loginUrlEmployee, employee)
  }
  loggedIn(){
    return !!localStorage.getItem("token")
  }
}
