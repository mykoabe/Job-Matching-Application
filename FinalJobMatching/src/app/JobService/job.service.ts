import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})

export class JobService {
  private _jobsUrl = "http://localhost:5000/api/jobs"

  constructor(private http: HttpClient) { }

  getJobs(){
    return this.http.get<any>(this._jobsUrl)
  }
  addJob(job){
    return this.http.post<any>(this._jobsUrl, job)
  }
}
