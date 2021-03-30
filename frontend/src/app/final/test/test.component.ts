import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss']
})

export class TestComponent implements OnInit {
  selectedfile = null;
  certificate_name: string;
  x: string;
  y: string;
  is_discription: string;
  discription: string;
  img: File;
  name;


  friends: [];
  constructor(private http: HttpClient,) { }

  ngOnInit(): void {
    this.http.get<any>("http://127.0.0.1:8000/portal/detailm/").subscribe(
      data => {
        console.log(data)
        this.name = data
        // localStorage.setItem('team_data', JSON.stringify(this.name))
      }
    )

  }


  onFileSelected(event) {
    console.log(event);
  }

  onFileSelectedSelected(event) {
    this.selectedfile = event.target.files[0];
  }
  // this.title = event.target.value;
  onNameChanged(event) {
    this.certificate_name = event.target.value;
  }
  onXSelected(event) {
    this.x = event.target.value;
  }
  onYSelected(event) {
    this.y = event.target.value;
  }
  // onDisSelected(event) {
  //   this.is_discription = event.target.value;
  // }
  onDiscSelected(event) {
    this.discription = event.target.value;
  }
  onUpload() {
    const uploadData = new FormData();
    uploadData.append('certificate_name', this.certificate_name);
    uploadData.append('x', this.x);
    uploadData.append('y', this.y);
    uploadData.append('is_discrin', this.is_discription);
    uploadData.append('discription', this.discription);
    uploadData.append('file', this.img);
    this.http.post('http://127.0.0.1:8000/portal/sample/', uploadData).subscribe(
      data => console.log(data),
      error => console.log(error)
    );
  }
}

