# Sentiment Analyze API
 
### Apiyi Çalıştırmak için yapmaznız gerekenler 

tar dosyasını yükleyelim
    
    docker load < sentiment_analyze_api.tar

sonrasında aşağıdaki komut ile image yüklenmiş mi diye bakabilirsiniz:
    
    docker images

Şimdi docker image'ını run edelim ve container'ı çalıştıralım. 

    docker run -d --restart always -p 8080:8080 sentiment_analyze_api

api kullanıma hazır 


## API'nin Başarısı Hakkında:

Gönderilen veri için oluşturulan modelin başarısı aşağıda gösterilmiştir.

NOT: Gönderilen veri tam olarak yeterli bir veri olmadığı için sonuçlar böyledir. Modelin doğruluğunu artırmak için daha fazla ve çeşitli veri toplanması gerekmektedir.

- Classifiacation Report

    ![Alt text](image-1.png)

- Confusion Matrix

    ![Alt text](image-2.png)