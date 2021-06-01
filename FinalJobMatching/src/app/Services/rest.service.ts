import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Works } from '../works';

@Injectable({
  providedIn: 'root'
})
export class RestService implements OnInit {

  constructor(private http : HttpClient) { }

  ngOnInit(){

  }
  private _workUrl = "http://127.0.0.1:5000/worksReport/"
  // workUrl : string = "http://127.0.0.1:5000/worksReport/";
  readWorks()
  {
    return this.http.get<[Works]>(this._workUrl);
  }

}
