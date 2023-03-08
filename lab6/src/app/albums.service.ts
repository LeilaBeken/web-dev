import { Injectable } from '@angular/core';
import { Photos } from './models';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AlbumsService {

  constructor(private client: HttpClient) { }

  getPhotos(): Observable<Photos[]>{
    return this.client.get<Photos[]>('https://jsonplaceholder.typicode.com/albums/1/photos');
  }
  getPhoto(id: number, title: string): Observable<Photos> {
    return this.client.get<Photos>(`https://jsonplaceholder.typicode.com/albums/1/photos/${id}`);
  }
}
