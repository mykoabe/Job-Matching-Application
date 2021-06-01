import { Component, OnInit } from '@angular/core';
import { JobService } from '../JobService/job.service';
@Component({
  selector: 'app-jobs',
  templateUrl: './jobs.component.html',
  styleUrls: ['./jobs.component.css']
})
export class JobsComponent implements OnInit {
  jobs = [];
  constructor(private _jobservice: JobService) { }
  ngOnInit(): void {
    this._jobservice.getJobs()
    .subscribe
      (
        res=>this.jobs = res, 
        err=>console.log(err)
      )
  }

}
